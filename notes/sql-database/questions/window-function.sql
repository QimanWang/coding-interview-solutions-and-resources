http://www.postgresqltutorial.com/postgresql-window-function/ 

CREATE TABLE qimandev.product_groups (
 group_id serial PRIMARY KEY,
 group_name VARCHAR (255) NOT NULL
);

CREATE TABLE qimandev.products (
 product_id serial PRIMARY KEY,
 product_name VARCHAR (255) NOT NULL,
 price DECIMAL (11, 2),
 group_id INT NOT NULL,
 FOREIGN KEY (group_id) REFERENCES qimandev.product_groups (group_id)
);

INSERT INTO qimandev.product_groups (group_name)
VALUES
 ('Smartphone'),
 ('Laptop'),
 ('Tablet');

INSERT INTO qimandev.products (product_name, group_id,price)
VALUES
 ('Microsoft Lumia', 1, 200),
 ('HTC One', 1, 400),
 ('Nexus', 1, 500),
 ('iPhone', 1, 900),
 ('HP Elite', 2, 1200),
 ('Lenovo Thinkpad', 2, 700),
 ('Sony VAIO', 2, 700),
 ('Dell Vostro', 2, 800),
 ('iPad', 3, 700),
 ('Kindle Fire', 3, 150),
 ('Samsung Galaxy Tab', 3, 200);

----- valdiate data
select * from qimandev.product_groups;
select * from qimandev.products;

-- get avg price
SELECT
 AVG (price)
FROM
qimandev.products;

-- get avg of each category
SELECT
 group_name,
 AVG (price)
FROM
qimandev.products
INNER JOIN qimandev.product_groups on qimandev.products.group_id = qimandev.product_groups.group_id
GROUP BY
 group_name;

-- instead of join id = id, we can use 'using (group_id)'
SELECT
 group_name,
 AVG (price)
FROM
qimandev.products
INNER JOIN qimandev.product_groups USING (group_id)
GROUP BY
 group_name;

-- so far the aggregate returns either 1 or n groups of data.
-- Smartphone	500
-- Tablet	350
-- Laptop	850

-- window on the other hand: returns value for each row in the window. each row is grouped into something.
SELECT
 product_name,
 price,
 group_name,
 AVG (price) OVER (PARTITION BY group_name)
FROM
qimandev.products
INNER JOIN qimandev.product_groups USING (group_id);
-- the avg is appended to every row of data in this window.


-- HP Elite	1200.00	Laptop	850
-- Lenovo Thinkpad	700.00	Laptop	850
-- Sony VAIO	700.00	Laptop	850
-- Dell Vostro	800.00	Laptop	850
-- Microsoft Lumia	200.00	Smartphone	500
-- HTC One	400.00	Smartphone	500
-- Nexus	500.00	Smartphone	500
-- iPhone	900.00	Smartphone	500
-- iPad	700.00	Tablet	350
-- Kindle Fire	150.00	Tablet	350
-- Samsung Galaxy Tab	200.00	Tablet	350

-- synatx:
-- window_function(arg1, arg2,..) OVER (PARTITION BY expression ORDER BY expression)
-- windows functions : row_number(), rank(), dense_rak(), aggregate functions, etc
-- partition by divide rows into group.
-- you can add order by for to sort each window set. first_value(),last_value(),nth_value()

-- below functions assigns integer values to rows based on their order.
-- row_number(): assign running serial number to rows in each partition.
SELECT
 product_name,
 group_name,
 price,
 ROW_NUMBER () OVER (
 PARTITION BY group_name
 ORDER BY
 price
 )
FROM
qimandev.products
INNER JOIN qimandev.product_groups USING (group_id);

-- Sony VAIO	Laptop	700.00	1
-- Lenovo Thinkpad	Laptop	700.00	2
-- Dell Vostro	Laptop	800.00	3
-- HP Elite	Laptop	1200.00	4
-- Microsoft Lumia	Smartphone	200.00	1
-- HTC One	Smartphone	400.00	2
-- Nexus	Smartphone	500.00	3
-- iPhone	Smartphone	900.00	4
-- Kindle Fire	Tablet	150.00	1
-- Samsung Galaxy Tab	Tablet	200.00	2
-- iPad	Tablet	700.00	3

-- rank(): assign ranking within an ordered partition.
-- if values are same, they get same rank and skips the next rank id.
SELECT
 product_name,
 group_name,
  price,
 RANK () OVER (
 PARTITION BY group_name
 ORDER BY
 price
 )
FROM
qimandev.products
INNER JOIN qimandev.product_groups USING (group_id);

-- Sony VAIO	Laptop	700.00	1
-- Lenovo Thinkpad	Laptop	700.00	1
-- Dell Vostro	Laptop	800.00	3
-- HP Elite	Laptop	1200.00	4
-- Microsoft Lumia	Smartphone	200.00	1
-- HTC One	Smartphone	400.00	2
-- Nexus	Smartphone	500.00	3
-- iPhone	Smartphone	900.00	4
-- Kindle Fire	Tablet	150.00	1
-- Samsung Galaxy Tab	Tablet	200.00	2
-- iPad	Tablet	700.00	3

-- dense_rank(): similar to rank, but doesn't skip rank sequence.


-- First_value,last_value
select *,
first_value(price) over ( partition by group_name order by price),
last_value(price) over ( partition by group_name  order by price RANGE BETWEEN current row AND unbounded following)
from qimandev.product_groups join qimandev.products using (group_id);
-- 2	Laptop	7	Sony VAIO	700.00	700	700
-- 2	Laptop	6	Lenovo Thinkpad	700.00	700	700
-- 2	Laptop	8	Dell Vostro	800.00	700	800
-- 2	Laptop	5	HP Elite	1200.00	700	1200
-- 1	Smartphone	1	Microsoft Lumia	200.00	200	200
-- 1	Smartphone	2	HTC One	400.00	200	400
-- 1	Smartphone	3	Nexus	500.00	200	500
-- 1	Smartphone	4	iPhone	900.00	200	900
-- 3	Tablet	10	Kindle Fire	150.00	150	150
-- 3	Tablet	11	Samsung Galaxy Tab	200.00	150	200
-- 3	Tablet	9	iPad	700.00	150	700

-- last_value(): defaults to RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
-- so we need to add : range between unbounded preceding and unbounded following


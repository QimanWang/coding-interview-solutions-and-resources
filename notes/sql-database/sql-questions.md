# eduerak video
https://www.youtube.com/watch?v=-WEpWH1NHGU

1. Diff between delete and truncate

- delete
  - remove one row
  - can be rolledback
  - Delete is Data Manipulation Language
  - Slower than Truncate

- truncate  
  - delete all row
  - cannot be rolledback
  - DDL
  - faster
  
2. Different lanuages

- DDL - define databse schema
- DML - manipulate tables
- DCL - premission
- TCL - controls transaction, rollback, etc

3. DBMS - database management system

4. table - row, columns. field are column names.

5. join - combine rows from 2 or more tables.

6. char vs varchar , varchar is not fixed.

7. primary key - unique row identifier

8. constraints - limit data while creating , aleter table. 
- not null, 
- unique,
- check,
- default,
- index: fast data retirval

9. sql vs mysql

10. unique key, id for a row, can be multiple value, can be null, cannot be duplicate.

11. foreign key maintains connection between 2 tables. foreign key in child table is used to reference primary key in parent table.

12. data integrity - business rule
- accurate
- consistent

13. clustered vs non clustered idnex. index is to make data retrival faster by altering the way data is stored.
- cluster index - faster, only 1 per table, sort out rows by the column. 
- non cluster - slower, can have many in 1 table. create seperate object that poitns back to the row after searching.

14. get current date - select getdate(), now()

15. join types:
- inner join
- full
- left
- right

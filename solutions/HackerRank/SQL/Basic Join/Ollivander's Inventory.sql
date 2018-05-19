/*
Hermione decides the best way to choose is by determining the minimum number of gold galleons needed to buy each non-evil wand of high power and age. Write a query to print the id, age, coins_needed, and power of the wands that Ron's interested in, sorted in order of descending power. If more than one wand has same power, sort the result in order of descending age.
*/

/*
when only wants to select the min of a column after joinging, we can use an inner select to select the min/max of that field and use colm = on the outer select.
*/

select id,age,coins_needed,power
from wands w join Wands_Property wp
    on w.code = wp.code
    where is_evil = 0 and
    coins_needed =
        (select min(coins_needed) from wands w1 join
        wands_property wp1 on w1.code = wp1.code
         where w1.power = w.power and wp1.age = wp.age)
    order by power desc,age desc;

/*
we first calculate earning, then count num occurance of that earnings
then we group it by that earning amount,
1 means the column idx for which the query returns
*/

select months*salary as earnings, count(*) from employee
group by 1 order by 1 desc limit 1;

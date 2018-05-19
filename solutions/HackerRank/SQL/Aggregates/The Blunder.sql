/*
first we need to calculate the actual average of the salaries
then we need to calculate the averages by remvoing the zeroes.
we can achieve that by simply replacing 0's with ''


*/

SELECT CEIL(AVG(SALARY) - AVG(REPLACE(SALARY,'0','')))
FROM EMPLOYEES;

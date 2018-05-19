/*
round will round to a decimal place
truncate will drop all value after decimal place
*/

select  round(sum(LAT_N),2),round(sum( LONG_W),2) from STATION 

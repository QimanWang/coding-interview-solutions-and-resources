/*
Enter your query here.
*/
select round((max(lat_n) - min(lat_N)) + (max(long_w) - min(long_w)),4) from station;

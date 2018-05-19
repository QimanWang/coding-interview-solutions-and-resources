/*

Enter your query here.
Query the smallest Northern Latitude (LAT_N) from STATION that is greater than . Round your answer to decimal places.
*/

select round(min(lat_n),4) from station where lat_N > 38.7780;

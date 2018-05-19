/*Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than .
Round your answer to  decimal places.
Enter your query here.
*/

select round(LONG_W,4) from STATION where LAT_N <137.2345 order by lat_n desc limit 1;

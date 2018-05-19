/* MySQL dont have medium built in.
medium is the value that seperat the higher half to lower half
so the data should be sorted, then we access the middle index
if odd amount of data, ex:13
13/2 = 6.5, we want the 7th data, so we round up
if even: 14
we want the avg of both
14/2 = 7,
we want the 7th and the 8th averaged together
*/
/*
Enter your query here.
first we sort the lat_n and append rowindx to each row
then we select the middle 2 row idx and avergae the two values
*/

set @rowidx := -1;

select round(avg(lat_n),4)
from
(select @rowidx := @rowidx +1 as rowidx,
    lat_n as lat_n
    from station
    order by lat_n asc) as sorted_lat_ns
    where
    rowidx in (floor(@rowidx/2), ceil(@rowidx/2));

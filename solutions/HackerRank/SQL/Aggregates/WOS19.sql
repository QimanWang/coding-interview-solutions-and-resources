/*
Enter your query here.
*/
select round(
    sqrt(
        power(
    (max(lat_n) - min(lat_N))
            ,2)
    +
        power(
    (max(long_w) - min(long_w))
            ,2)
        )/* sqrt*/
    ,4) from station;

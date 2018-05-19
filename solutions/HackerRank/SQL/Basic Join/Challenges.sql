/*
good problem, break the problem up into sub problems

*/


select h.hacker_id, name, count(h.hacker_id) as challenges_created
from hackers h join challenges c
    on h.hacker_id = c.hacker_id
    group by h.hacker_id, name
    having

    /* output anyone with a count that is equal to... */
    challenges_created =
        /* the max count that anyone has */
        (SELECT MAX(freq_table.freq)
        from (SELECT COUNT(hacker_id) as freq
             from challenges
             group by hacker_id
             order by hacker_id) freq_table)

    /* or anyone who's count is in... */
    or challenges_created in
        /* the set of counts... */
        (select t.cnt
         from (select count(*) as cnt
               from challenges
               group by hacker_id) t
         /* who's group of counts... */
         group by t.cnt
         /* has only one element */
         having count(t.cnt) = 1)



    order by challenges_created desc, c.hacker_id;

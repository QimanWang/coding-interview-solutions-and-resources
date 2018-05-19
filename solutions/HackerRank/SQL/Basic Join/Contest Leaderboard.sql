/*
The total score of a hacker is the sum of their maximum scores for all of the challenges. Write a query to print the hacker_id, name, and total score of the hackers ordered by the descending score. If more than one hacker achieved the same total score, then sort the result by ascending hacker_id. Exclude all hackers with a total score of  from your result.
*/
/* return h.id,h.name, total score*/
select h.hacker_id, h.name, sum(score) as total_score
from hackers h join
/*    submissions s on  h.hacker_id = s.hacker_id */
/* we need to join the hackers on the max score of the submision table)*/
    (select hacker_id, max(score) as score
        from submissions
        group by hacker_id, challenge_id) max_score
     on h.hacker_id = max_score.HACKER_ID
     group by h.hacker_id, h.name
     having total_score >0
     order by total_score desc, h.hacker_id;

/* */
     select h.hacker_id, name, sum(score) as total_score
     from
     hackers as h inner join
     /* find max_score*/
     (select hacker_id,  max(score) as score from submissions group by challenge_id, hacker_id) max_score

     on h.hacker_id=max_score.hacker_id
     group by h.hacker_id, name

     /* don't accept hackers with total_score=0 */
     having total_score > 0

     /* finally order as required */
     order by total_score desc, h.hacker_id
     ;

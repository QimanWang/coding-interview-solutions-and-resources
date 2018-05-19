select  s.hacker_id, h.name
from hackers h
    join submissions s on
        s.hacker_id  = h.hacker_id
    join challenges c on
        c.challenge_id = s.challenge_id
    join difficulty d on
        d.difficulty_level = c.difficulty_level
    where
        s.score = d.score
    group by s.hacker_id, h.name
    having count(s.hacker_id) >1
    ORDER BY COUNT(S.HACKER_ID) DESC, h.HACKER_ID ASC

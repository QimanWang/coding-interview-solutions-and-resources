select CONCAT(Name, '(', LEFT(Occupation, 1) , ')')
from occupations order by name;

select CONCAT('There are a total of ', count(*), ' ',LOWER(occupation),'s.')
from occupations
group by occupation
order by count(occupation) asc ,occupation;
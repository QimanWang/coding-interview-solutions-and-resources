-- comments
-- we want to create a pivot table that has x the occupation types 
-- y vaules of the names assocaited wit the names
-- we see that some columns will contains nulls because not every columns
-- has the same amoutn of people in that occupation. 
-- x-values: the 4 cooupations (Actor, Doctor, Professor, Singer)
-- the y-values will varies because the frequency is diferent
-- so the y-values contains the names, one per row

-- we first need 
-- then we count iterate through every row in occupations and increase counter col 
-- for every corresponding column name, then we append that name to the corresponding col
-- we will get n rows for n entries in occupations tables
-- each row will contain a name in one col and null in rest

-- then we select the min from every column 
-- if we dont use group by, we only get 1 row of data.
-- so group by will return a data for every row count

set @colDoc=0, @colProf=0, @colSingr=0, @colActr=0;

select min(Doctor), min(Professor), min(Singer), min(Actor)
from(
	select case when Occupation = 'Doctor' then (@colDoc:=@colDoc+1)
				when Occupation = 'Professor' then (@colProf:=@colProf+1)
				when Occupation = 'Singer' then (@colSingr:=@colSingr+1)
				when Occupation = 'Actor' then (@colActr:=@colActr+1) end as rowNumber,
		case when Occupation = 'Doctor' then Name end as Doctor,
		case when Occupation='Professor' then Name end as Professor,
		case when Occupation='Singer' then Name end as Singer,
		case when Occupation='Actor' then Name end as Actor
		
	from occupations
	order by name
) Temp
group by rowNumber;			
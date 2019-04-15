# eduerak video
https://www.youtube.com/watch?v=-WEpWH1NHGU
1. Diff between delete and truncate


- delete
  - remove one row
  - can be rolledback
  - Delete is Data Manipulation Language
  - Slower than Truncate

- truncate  
  - delete all row
  - cannot be rolledback
  - DDL
  - faster
  
2. Different lanuages

- DDL - define databse schema
- DML - manipulate tables
- DCL - premission
- TCL - controls transaction, rollback, etc

3. DBMS - database management system

4. table - row, columns. field are column names.

5. join - combine rows from 2 or more tables.

6. char vs varchar , varchar is not fixed.

7. primary key - unique row identifier

8. constraints - limit data while creating , aleter table. 
- not null, 
- unique,
- check,
- default,
- index: fast data retirval

9. sql vs mysql

10. unique key, id for a row, can be multiple value, can be null, cannot be duplicate.

11. foreign key maintains connection between 2 tables. foreign key in child table is used to reference primary key in parent table.

12. data integrity - business rule
- accurate
- consistent

13. clustered vs non clustered idnex. index is to make data retrival faster by altering the way data is stored.
- cluster index - faster, only 1 per table, sort out rows by the column. 
- non cluster - slower, can have many in 1 table. create seperate object that poitns back to the row after searching.

14. get current date - select getdate(), now()

15. join types:
- inner join
- full
- left
- right

16. denormalization - increase performance by removing reduncy into a table. techinique to access higher to lower form of data.

17. enity - a single table, which contains attributes.
- relationships : link between 2 entity.

18. index 
- performance tuning method, faster retrivial
- create an entry for every value

19. diff type of index:
- index? //TODO

20. normalization:
- process of organzing data to avoid duplication and redundancy

21. drop vs truncate
- drop : removes table and cannot be rolled back.
- truncate : removes all the rows of a table.

22. Normalization : 
- 1NF : all record is unique. this will expand the table size.
- 2NF : single column primary key, if there's dupe, you will create a new table to link.
- 3NF : no transitive dependencies. only dpeend on primary
- BCNF : only 1 candidate key.

23. ACID
- Atomicity: a trans will fial and all will fail
- Consistency: always complete
- Isolation: concurrency control
- Duraity : commited will echo?

24. Trigger: special stored procedure to run on data modification.
- Before,after insert
- update
- delete

25. 5 types of operator

26. null : is not 0 or blank. null is unavailable, unknown.

27. Cross join vs natural join : 
- cross join : cartersian product
- all column have same name

28. Subquery : 

29. correlated subquery : 
- non - correlated : //TODO

33. group functions: avg,count,max,min,sum,variance

34. relationship : 1-1,1-many,many-1,self-referencing

36. between : range, in : in set.

37. merge : allow conditional update or insert of data into a table.

38. clause : where, having to limit result set by a condition.

39. executing dynamic sql : write query with paparm, using exec, sp_executesql

44. column level contraint, table level constraint.

45. case manipulation: lower, upper, incap - first letter cap.

46. set Operators
- union : all left and right.
- intersect: only common
- minus : only left minus right common.

47. alias : renaming

48. aggregate function, max(), count(), 
- scalar function ucase(), now()

49. how to fetch alternate.

52. substring 

53. view : virtual table, takes less space.
    
54. stored prodecure : made up of sql statements. combine.

55. stored procedure.
- advantage: 
- disadvanatge : can only be executed in database and more memory.
  
58. collation: rule define how data can be compared.
    
59. datawarehouse : central data repo, datamart is a subset.

60. stuff and replace functions.


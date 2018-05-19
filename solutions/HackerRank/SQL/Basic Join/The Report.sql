/*
first way doesn't require the grade table
*/

select
    case
    when marks/10 >= 7 then name
    else NULL
    end as n,
    least(10,truncate(marks/10 +1,0)) as m,
    marks
    from students
    order by m desc, name, marks asc

/*
second way:
we join both tables and see use the grades
*/

/*
Enter your query here.
*/

select if(grade <8 , NULL, name), Grades.grade, students.marks
    from students join grades on
        students.marks >= grades.min_mark and
        students.marks <= grades.max_mark
    order by grades.grade desc, students.name, students.marks asc;

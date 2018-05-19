select
Case 
    when a+b <= c then "Not A Triangle"
    when a+c <= b then "Not A Triangle"
    when b+c <= a then "Not A Triangle"
    
    when a=b AND b=c then "Equilateral"
    
    when a=b and a <> c then "Isosceles"
    when a=c and a <> b then "Isosceles"
    when b=c and b <> a then "Isosceles"
    
    else "Scalene"
    END
from Triangles;
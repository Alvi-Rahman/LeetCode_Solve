# Write your MySQL query statement below
SELECT (SELECT DISTINCT Salary From Employee
ORDER BY SALARY DESC LIMIT 1 OFFSET 1) as SecondHighestSalary ;
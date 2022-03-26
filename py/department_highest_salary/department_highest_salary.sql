SELECT t.Department, t.Employee, t.Salary 
FROM 
  (SELECT d.name as Department, e.name as Employee, e.salary as Salary, RANK()
  OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) salary_rank
  FROM Employee e
  JOIN Department d
  WHERE e.departmentId = d.id) AS t
WHERE t.salary_rank = 1;

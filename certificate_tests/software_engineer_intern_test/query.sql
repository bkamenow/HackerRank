SELECT
    e1.employee_name AS lesser_earning_employee,
    e2.employee_name AS higher_earning_employee
FROM
    employee e1
JOIN
    employee e2 ON e1.salary < e2.salary
ORDER BY
    e1.employee_id ASC,
    e2.salary ASC;

# Write your MySQL query statement below
select e.employee_id,e.name,count(f.age) as reports_count,round(avg(f.age),0) as average_age

    from Employees e

    join(
        select reports_to,age
        from Employees
    ) f
    on e.employee_id = f.reports_to
    group by e.employee_id,e.name
    order by e.employee_id;
# Write your MySQL query statement below

select  p.project_id , 
        ifnull(
            round(sum(e.experience_years) / count(p.project_id),
            2),0
        ) as average_years
    from Project p
    left join Employee e
    on e.employee_id = p.employee_id
    group by  project_id;
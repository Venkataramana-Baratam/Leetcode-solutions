# Write your MySQL query statement below

select s.user_id ,ROUND(
        IFNULL(
            SUM(c.action = 'confirmed') / COUNT(c.action),
            0
        ),
        2
    ) AS confirmation_rate
from Signups s
left join Confirmations c
on s.user_id = c.user_id
group by s.user_id;

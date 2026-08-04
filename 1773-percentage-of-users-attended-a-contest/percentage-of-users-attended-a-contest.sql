SELECT 
    r.contest_id,
    IFNULL(
        ROUND(
            COUNT(r.user_id) * 100.0 / (SELECT COUNT(*) FROM Users),
            2
        ),
        0
    ) AS percentage
FROM Register r
LEFT JOIN Users u
ON u.user_id = r.user_id
GROUP BY r.contest_id
ORDER BY percentage DESC, contest_id ASC;
'''
    SELECT
        r.user_id,
        SUM(r2.reward) AS reward_sum_2022
    FROM
        reports r
    JOIN
        reports r2 ON r.user_id = r2.user_id
    WHERE
        DATE_PART('year', r.created_at) = 2021
        AND r.created_at = (SELECT MIN(r3.created_at)
                            FROM reports r3
                            WHERE r3.user_id = r.user_id)
        AND DATE_PART('year', r2.created_at) = 2022
    GROUP BY
        r.user_id;
'''

-- 1. Initial Exploratory Data Analysis

-- 1.1 Can a user show up more than once in the activity table? - Yes
SELECT uid, COUNT(*) AS user_activity
FROM activity
GROUP BY uid
HAVING COUNT(*) > 1;

-- 1.2 Do we expect all users to make a purchase? - No
-- Do we want to include users regardless of whether they make a purchase? - Yes
SELECT *
FROM users u
LEFT JOIN activity a ON u.id = a.uid;

-- 1.3 What are the start and end dates of the experiment?
SELECT MIN(join_dt) AS start_date, MAX(join_dt) AS end_date
FROM groups;

-- 1.4 How many total users were in the experiment?
SELECT COUNT(DISTINCT uid) AS total_users
FROM groups;

-- 1.5 How many users were in the control and treatment groups?
SELECT "group", COUNT(uid) AS users_per_group
FROM groups
GROUP BY "group";

-- 1.6 What was the conversion rate of all users?
SELECT ROUND( (SELECT COUNT(DISTINCT uid) FROM activity)::numeric / COUNT(uid) * 100, 2) AS conversion_rate
FROM groups;

-- 1.7 What is the user conversion rate for the control and treatment groups?
SELECT "group", ROUND(COUNT(DISTINCT a.uid)::numeric / COUNT(g.uid)::numeric * 100, 2) AS conversion_rate
FROM groups g
LEFT JOIN activity a ON a.uid = g.uid
GROUP BY "group";

-- 1.8 Average amount spent per user by group, including users who did not convert
WITH spent AS (
    SELECT uid, SUM(spent) AS spend
    FROM activity
    GROUP BY uid
)
SELECT g.group, ROUND(AVG(COALESCE(s.spend, 0)), 3) AS avg_spend
FROM groups g
LEFT JOIN spent s ON g.uid = s.uid
GROUP BY g.group;

-- 2. Data Extract to Tableau - Exploratory Visualisation & Python for Hypothesis Testing
WITH cte_conversion AS (
    SELECT g.uid,
           SUM(COALESCE(spent, 0)) AS spend,
           CASE WHEN SUM(COALESCE(spent, 0)) > 0 THEN 'converted' ELSE 'not_converted' END AS conversion
    FROM groups g
    LEFT JOIN activity a ON g.uid = a.uid
    GROUP BY g.uid
)
SELECT c.uid,
       COALESCE(u.country, 'Unknown') AS country,
       COALESCE(u.gender, 'Unknown') AS gender,
       COALESCE(g.device, 'Unknown') AS device,
       g.group,
       c.spend,
       c.conversion
FROM cte_conversion c
LEFT JOIN groups g ON c.uid = g.uid
LEFT JOIN users u ON c.uid = u.id;

-- 3. Data Extract to Tableau - Novelty Effects
WITH cte_conversion AS (
    SELECT g.uid,
           MIN(a.dt) AS dt,
           SUM(COALESCE(spent, 0)) AS spend,
           CASE WHEN SUM(COALESCE(spent, 0)) > 0 THEN 'converted' ELSE 'not_converted' END AS conversion
    FROM groups g
    LEFT JOIN activity a ON g.uid = a.uid
    GROUP BY g.uid
)
SELECT c.uid,
       g.join_dt,
       c.dt,
       COALESCE(u.country, 'Unknown') AS country,
       COALESCE(u.gender, 'Unknown') AS gender,
       COALESCE(g.device, 'Unknown') AS device,
       g.group,
       c.spend,
       c.conversion
FROM cte_conversion c
LEFT JOIN groups g ON c.uid = g.uid
LEFT JOIN users u ON c.uid = u.id;


-- a script that lists all shows from hbtn_0d_tvshows_rate by their rating.

-- The Query
SELECT tv_shows.title AS title, SUM(rate) AS rating
FROM tv_shows
JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.id
ORDER BY 2 desc;

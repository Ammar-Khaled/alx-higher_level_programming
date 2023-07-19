-- a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- The Query
SELECT tv_genres.name AS name, SUM(tv_show_ratings.rate) AS rating
FROM tv_genres
JOIN tv_show_genres
ON tv_genres = tv_show_genres.genre_id
JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
JOIN tv_show_ratings
ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_show_ratings.show_id
ORDER BY 2 desc;

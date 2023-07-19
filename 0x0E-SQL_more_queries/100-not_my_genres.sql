-- a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- The Query
SELECT tv_genres.name AS name
FROM tv_genres
LEFT JOIN
(SELECT tv_genres.id id, tv_genres.name name
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = "Dexter"
ORDER BY 1;
) dexter_genres
ON tv_genres.id = dexter_genres.id
WHERE dexter_genres.id is NULL
ORDER BY 1;

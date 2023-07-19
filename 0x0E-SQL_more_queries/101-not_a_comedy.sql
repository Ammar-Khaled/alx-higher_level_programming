-- Script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT tv_shows.title AS title  -- Query to get shows that not belong to Comedy genre
FROM tv_shows
LEFT JOIN
(
	SELECT tv_genres.id, tv_genres.name -- Query to get Comdey shows
	FROM tv_genres
	JOIN tv_show_genres
	     ON tv_genres.id = tv_show_genres.genre_id
	JOIN tv_shows
	     ON tv_show_genres.show_id = tv_shows.id
	WHERE tv_genres.name = "Comedy"
	ORDER BY tv_genres.id
) Comedy_shows ON Comedy_shows.id = tv_shows.id
WHERE Comedy_shows.id is NULL
ORDER BY tv_shows.title;

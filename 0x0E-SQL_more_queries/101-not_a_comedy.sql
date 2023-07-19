-- Script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows
SELECT tv_shows.title AS title  -- Query to get shows that not belong to Comedy genre
FROM tv_shows
LEFT JOIN
(
	SELECT tv_shows.title -- Query to get Comdey shows
	FROM tv_shows
    JOIN tv_show_genres
    ON tv_show_genres.show_id = tv_shows.id
    JOIN tv_genres
    ON tv_genres.id = tv_show_genres.genre_id
	WHERE tv_genres.name = "Comedy"
	ORDER BY tv_shows.title
) Comedy_shows ON Comedy_shows.title = tv_shows.title
WHERE Comedy_shows.title is NULL
ORDER BY tv_shows.title;

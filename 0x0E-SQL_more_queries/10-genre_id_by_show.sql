-- a script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.

-- The Query
SELECT sh.id, g.show_id
FROM tv_shows sh
JOIN tv_show_genres g
ON sh.id = g.show_id
ORDER BY sh.title, g.show_id;

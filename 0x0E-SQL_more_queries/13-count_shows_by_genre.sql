-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT genres.genre AS genre, COUNT(tv_shows.id) AS number_of_shows
FROM genres
LEFT JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
LEFT JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
GROUP BY genres.genre
HAVING COUNT(tv_shows.id) > 0
ORDER BY number_of_shows DESC;

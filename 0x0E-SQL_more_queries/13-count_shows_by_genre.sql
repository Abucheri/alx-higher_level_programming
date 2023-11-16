-- This script lists all genres in the specified MySQL database and displays the number of shows linked to each genre.
-- List all genres with the number of shows linked using one SELECT statement
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
  FROM tv_genres
       LEFT JOIN tv_show_genres
       ON tv_genres.id = tv_show_genres.genre_id
  GROUP BY tv_genres.id
  HAVING number_of_shows > 0
  ORDER BY number_of_shows DESC;

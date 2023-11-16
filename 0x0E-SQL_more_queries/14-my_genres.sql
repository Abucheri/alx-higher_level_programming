-- This script lists all genres of the show Dexter from the specified MySQL database.
-- List all genres of the show Dexter using one SELECT statement
SELECT tv_genres.name
  FROM tv_genres
       JOIN tv_show_genres
       ON tv_genres.id = tv_show_genres.genre_id

       JOIN tv_shows
       ON tv_show_genres.show_id = tv_shows.id
  WHERE tv_shows.title = 'Dexter'
  ORDER BY tv_genres.name ASC;

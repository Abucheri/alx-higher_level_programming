-- This script lists all genres not linked to the show Dexter from the specified MySQL database.
SELECT DISTINCT tv_genres.name
  FROM tv_genres
  WHERE tv_genres.id NOT IN
        (SELECT tv_genres.id
	   FROM tv_shows
	        JOIN tv_show_genres
		ON tv_shows.id = tv_show_genres.show_id

		JOIN tv_genres
		ON tv_show_genres.genre_id = tv_genres.id
	   WHERE tv_shows.title = 'Dexter')
  ORDER BY tv_genres.name ASC;

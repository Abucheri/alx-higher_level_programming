-- This script lists all shows in the specified MySQL database along with their genre IDs.
-- List all shows along with their genre IDs using one SELECT statement
SELECT tv_shows.title, tv_show_genres.genre_id
  FROM tv_shows
       LEFT JOIN tv_show_genres
       ON tv_shows.id = tv_show_genres.show_id
  ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;

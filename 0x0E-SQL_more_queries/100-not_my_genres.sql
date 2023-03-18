-- A script that uses the  hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
SELECT DISTINCT g.`name`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS s
       ON g.`id` = s.`genre_id`

       INNER JOIN `tv_shows` AS t
       ON s.`show_id` = t.`id`
       WHERE g.`name` NOT IN
             (SELECT `name`
                FROM `tv_genres` AS g
	             INNER JOIN `tv_show_genres` AS s
		     ON g.`id` = s.`genre_id`

		     INNER JOIN `tv_shows` AS t
		     ON s.`show_id` = t.`id`
		     WHERE t.`title` = "Dexter")
 ORDER BY g.`name`;
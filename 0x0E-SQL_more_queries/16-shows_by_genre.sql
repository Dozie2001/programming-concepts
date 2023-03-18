-- A script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
SELECT s.`title`, g.`name`
    FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` as t
          ON s.`id` = t.`show_id`
        LEFT JOIN `tv_genres` AS g
           ON g.`id` = t.`genre_id`
ORDER BY s.`title`, g.`name`;

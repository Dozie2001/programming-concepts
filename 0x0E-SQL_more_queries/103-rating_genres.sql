-- A script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
SELECT g.`name`,
   SUM(r.`rate`) AS `rating`
   FROM `tv_genres` AS g
      INNER JOIN `tv_show_genres` AS t
        ON g.`id` = t.`genre_id`
    INNER JOIN `tv_show_ratings` AS r
      USING (`show_id`)
    GROUP BY g.`name`
    ORDER BY `rating` DESC;

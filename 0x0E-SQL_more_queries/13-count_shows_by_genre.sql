-- A script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- Second column must be called number_of_shows
-- Results must be sorted in descending order by the number of shows linked
SELECT g.`name` AS `genre`,
    COUNT(*) AS `number_of_shows`
  FROM `tv_genre` AS g 
    INNER JOIN `tv_show_genres` AS t
    ON g.`id` = t.`genre_id`
GROUP BY `genre`
ORDER BY `number_of_shows`;
-- List top 100 MOVIES from the database (ordered by the rating)
SELECT title, rating
FROM movies
JOIN ratings
ON ratings.movie_id = movies.id
WHERE id IN
(SELECT movie_id
FROM ratings
ORDER BY rating DESC LIMIT 100); -- Nested query
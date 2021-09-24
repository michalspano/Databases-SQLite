-- Print movies with rating of 10 (ordered alphabetically)
SELECT title
FROM movies
WHERE movies.id IN
(SELECT ratings.movie_id
FROM ratings
WHERE ratings.rating = 10)
ORDER BY movies.title;
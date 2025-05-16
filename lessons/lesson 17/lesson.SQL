SELECT i_author, name, birth_year 
FROM Authors;

-- not all fields
SELECT birth_year 
FROM Authors;

SELECT * 
FROM Authors;

SELECT name AS 'Author name' -- alias
FROM Authors;


-- WHERE -------------------
SELECT name 
FROM Authors
WHERE birth_year > 1900
;

SELECT * 
FROM Authors
WHERE ( birth_year > 1799 AND birth_year < 1900 ) OR birth_year = 1775
;

SELECT * 
FROM Authors
WHERE ( birth_year BETWEEN 1799 AND 1900 ) OR birth_year IN ( 1775 )
;

SELECT * 
FROM Authors
WHERE length(name) > 11
;

SELECT * 
FROM Authors
ORDER BY birth_year
-- ASC за замовчуванням
-- DESC від найбільшого до найменшого
-- ASC від найменшого до найбільшого
;

SELECT 1 
FROM Authors
LIMIT 1
;

SELECT 1 
FROM Authors
LIMIT 1
OFFSET 4
;

SELECT *
FROM Authors 
JOIN Books ON Books.i_author = Authors.i_author
;

SELECT  B.title,
        B.publication_year,
        B.pages,
        A.name,
        G.genre_name
FROM Authors A
JOIN Books B ON B.i_author = A.i_author
JOIN Genres G ON B.i_genre = G.i_genre
;

SELECT  B.title,
        B.publication_year,
        B.pages,
        A.name,
        G.genre_name
FROM Authors A
JOIN Books B ON B.i_author = A.i_author
JOIN Genres G ON B.i_genre = G.i_genre
WHERE B.publication_year BETWEEN 1950 AND 2000
ORDER BY pages
LIMIT 3
OFFSET 1
;

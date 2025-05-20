-- агрегація
SELECT COUNT(i_book)
FROM Books;

SELECT count(1)
FROM Books;

SELECT count(pages) AS 'total_books',
       max(pages) AS 'max_pages', 
       min(pages) AS 'min_pages',
       avg(pages) AS 'avg_pages',
       sum(pages) AS 'total_pages'
FROM Books;

SELECT G.genre_name,
       Count(*) AS 'books_total'
  FROM Genres G
  JOIN Books B
    ON B.i_genre = G.i_genre
 GROUP BY G.genre_name
;

SELECT A.name AS 'author_name',
       AVG(B.pages) AS 'avg_pages'
  FROM Authors A
  JOIN Books B
    ON A.i_author = B.i_author
 GROUP BY A.name
 HAVING avg_pages > 300
 ORDER BY avg_pages
;

SELECT A.name,
       COUNT(B.i_book) AS 'total_books',
       AVG(B.pages) AS 'avg_pages'
  FROM Authors A
  JOIN Books B
    ON A.i_author = B.i_author
 GROUP BY A.name
  HAVING total_books > 1 AND avg_pages > 500
;

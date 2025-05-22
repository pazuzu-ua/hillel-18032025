SELECT A.name AS 'author_name',
       AVG(B.pages) AS 'avg_pages',
       SUM(B.pages) AS 'total_pages',
       COUNT(B.i_book) AS 'total_books'
  FROM Authors A
  JOIN Books B
    ON A.i_author = B.i_author
 GROUP BY A.name
 HAVING avg_pages < 350
 ORDER BY avg_pages
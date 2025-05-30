SELECT name, count(name) as 'Books count', sum(pages) as 'Summary pages', avg(pages) as 'Average pages'
FROM Books
INNER JOIN main.Authors A on A.i_author = Books.i_author
INNER JOIN main.Genres G on G.i_genre = Books.i_genre
group by name
having avg(pages) < 350;


SELECT count()
FROM Authors
WHERE birth_year < 1900

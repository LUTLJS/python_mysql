
DELIMITER $$

USE python_mysql$$

CREATE PROCEDURE find_all()
BEGIN
 SELECT title, isbn, CONCAT('first_name',' ','last_name') AS author
 FROM books
 INNER JOIN book_author ON book_author.book_id = books.id
 INNER JOIN AUTHORS ON book_author.author_id = authors.id;
END $$

DELIMITER ;
CALL find_all();


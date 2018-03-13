from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def delete_book(book_id):
	#read database configuration
	db_config = read_db_config()

	#prepare query and data
	query = "DELETE FROM books WHERE id = %s"

	try:
		conn =MySQLConnection(**db_config)
		#update book title
		cursor = conn.cursor()
		cursor.execute(query, (book_id,))

		#accept the changes
		conn.commit()

	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()

if __name__ == '__main__':
	delete_book(86)
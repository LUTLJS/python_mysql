"""When I first used "VALUES(%s,%s)",it didn't work,then I used "VALUES(%d,%d)",and it surely didn't.Fianlly I used "VALUES(%s,%s)",and itworked.
What kind of magic was that.

"""
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def insert_books(books):
	query = ("INSERT INTO books""(title, isbn)""VALUES(%s,%s)")

	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor =conn.cursor()
		cursor.executemany(query, books)

		conn.commit()

	except Error as e:
		print('Error:', e)

	finally:
		cursor.close()
		conn.close()

def main():
	books = [('Harry Potter And The Order of The Phoenix', '9780439358071'),
	('Gone With the Wind', '9780446675536'), ('Pride and Prejudice (Modern Library Classics)', '9780679783268')]
	insert_books(books)

if __name__ == '__main__':
	main()


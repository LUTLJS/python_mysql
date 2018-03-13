
from mysql.connector import MySQLConnection,Error
from python_mysql_dbconfig import read_db_config
import os


def write_file(data, filename):
	with open(filename, 'wb') as f:
		f.write(b'data')

def read_blob(author_id, filename):
	query = "SELECT photo FROM authors WHERE id = %s"

	db_config = read_db_config()

	try:
		conn = MySQLConnection(**db_config)
		cursor = conn.cursor()
		cursor.execute(query, (author_id,))
		photo = cursor.fetchone()

		write_file(photo, filename)

	except Error as e:
		print(e)

	finally:
		cursor.close()
		conn.close()
def main():
	read_blob(144,"pictures\garth_stein.jpg")

if __name__ == '__main__':
	main()
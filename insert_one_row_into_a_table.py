"""When I first used "VALUES(%s,%s)",it didn't work,then I used "VALUES(%d,%d)",and it surely didn't.Fianlly I used "VALUES(%s,%s)",and itworked.
What kind of magic was that.

"""
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def insert_book(title, isbn):
	query = ("INSERT INTO books""(title,isbn)""VALUES(%s,%s)")
	args = (title, isbn)

	try:
		db_config = read_db_config()
		conn = MySQLConnection(**db_config)

		cursor = conn.cursor()
		cursor.execute(query, args)

		if cursor.lastrowid:
			print('last insert id',cursor.lastrowid)
		else:
			print('last insert id not found')

		conn.commit()

	except Error as error:
		print(error)

	finally:
		cursor.close()
		conn.close()

def main():
	insert_book('A Sudden Light', '9781439187036')

if __name__ == '__main__':
	main()



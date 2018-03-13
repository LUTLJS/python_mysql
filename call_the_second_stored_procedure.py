from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def call_find_by_isbn():
	try:
	
		db_config = read_db_config()
		conn =MySQLConnection(**db_config)
		cursor = conn.cursor()

		args = ['1236400967773',0]
		result_args = cursor.callproc('find_by_isbn', args)

		#print out the result
		print(result_args[1])
		
	except Error as e:
		print(e)

	finally:
		cursor.close()
		conn.close()

if __name__ == '__main__':
	call_find_by_isbn()
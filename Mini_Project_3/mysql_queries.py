import mysql.connector
import sys
"""
based on code from: https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-select.html
"""
def mysql_queries():
	try:
		print("Most Popular Tags: ")
		file = open('/home/jsneal/Desktop/API_Keys/MySQL/password.txt', 'r') # The file where my API keys were stored.
		password = file.readline()
		cnx = mysql.connector.connect(user='root', password=password,
                            		  host='127.0.0.1',
                            		  database='Mini_Project_3'
                            		  )
		cursor = cnx.cursor()
		try:	# need this if an image doesn't get labels
			query = "SELECT DISTINCT TAG, COUNT(*) FROM IMAGE_TAGS GROUP BY TAG ORDER BY COUNT(*) DESC"
			cursor.execute(query)

			for field in cursor:
  				print("{}, {}".format(
    			field[0], field[1]))

		except:
			print("Query failed!")

		cnx.commit()

		cursor.close()
		cnx.close()
		print('MySQL query executed!')
	except:
		print(sys.exc_info())
		print('mysql_queries error!')

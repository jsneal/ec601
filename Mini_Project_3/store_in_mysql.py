import mysql.connector
"""
Based on code from: https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html
"""
def store_in_mysql(username, dateAccessed, screenName, labels_per_image, image_list):
	try:
		file = open('/home/jsneal/Desktop/API_Keys/MySQL/password.txt', 'r') # The file where my API keys were stored.
		password = file.readline()
		cnx = mysql.connector.connect(user='root', password=password,
                              host='127.0.0.1',
                              database='Mini_Project_3'
                              )
		cursor = cnx.cursor()
		imageCounter = 0
		for image in image_list:
			add_image = ("INSERT INTO IMAGES "
               "(username, access_date, twitter_feed_handle, image_location) "
               "VALUES (%s, %s, %s, %s)")

			data_image = (username, dateAccessed, screenName, image)

			cursor.execute(add_image, data_image)
			for tag in labels_per_image[imageCounter]:

				add_image_tag = ("INSERT INTO IMAGE_TAGS "
              	"(twitter_feed_handle, image_location, tag) "
              	"VALUES (%s, %s, %s)")

				data_image_tag = (screenName, image, tag)

				cursor.execute(add_image_tag, data_image_tag)
			imageCounter+=1

		cnx.commit()

		cursor.close()
		cnx.close()
		print('Data stored in local MySQL database!')
	except:
		print('MySQL Module Error!')
	return
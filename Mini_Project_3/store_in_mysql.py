import mysql.connector

#def store_in_mysql(username, dateAccessed, screenName, labels_per_image, image_list):
file = open('/home/jsneal/Desktop/API_Keys/MySQL/password.txt', 'r') # The file where my API keys were stored.
password = file.readline()[0:-1]
cnx = mysql.connector.connect(user='root', password=password,
                              host='127.0.0.1',
                              database='Mini_Project_3')
cursor = cnx.cursor()

add_image = ("INSERT INTO IMAGES "
               "(username, access_date, twitter_feed_handle, image_location) "
               "VALUES (%s, %s, %s, %s)")

data_image = ('jsneal', 'tomorrow', 'jsneal', 'here')

cursor.execute(add_image, data_image)

cnx.commit()

cursor.close()
cnx.close()
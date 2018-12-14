from pymongo import MongoClient
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
import sys
"""
#Based on code from: https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb
"""
def store_in_mongo(username, dateAccessed, screenName, labels_per_image, image_list):
	try:
		file = open('/home/jsneal/Desktop/API_Keys/MongoDB/password.txt', 'r') # The file where my API keys were stored.
		password = file.readline()
		mongoStr = 'mongodb://jsneal:'+ password +'@miniproject3-shard-00-00-ggtat.gcp.mongodb.net:27017,miniproject3-shard-00-01-ggtat.gcp.mongodb.net:27017,miniproject3-shard-00-02-ggtat.gcp.mongodb.net:27017/images?ssl=true&replicaSet=MiniProject3-shard-0&authSource=admin&retryWrites=true'
		imageClient = MongoClient(mongoStr)
		dbImages = imageClient.images
		images = dbImages.images

		mongoStr = 'mongodb://jsneal:'+ password +'@miniproject3-shard-00-00-ggtat.gcp.mongodb.net:27017,miniproject3-shard-00-01-ggtat.gcp.mongodb.net:27017,miniproject3-shard-00-02-ggtat.gcp.mongodb.net:27017/image_tags?ssl=true&replicaSet=MiniProject3-shard-0&authSource=admin&retryWrites=true'
		image_tagsClient = MongoClient(mongoStr)
		dbImage_tags = image_tagsClient.image_tags
		image_tags = dbImage_tags.image_tags

		imageCounter = 0
		for image in image_list:
			try:	# need this if an image doesn't get labels
				image_data = {
    				'username': str(username),
    				'access_date': str(dateAccessed),
    				'twitter_feed_handle': str(screenName),
    				'image_location': str(image)
				}

				result = images.insert_one(image_data)

				for tag in labels_per_image[imageCounter]:

					image_tag_data = {
    					'twitter_feed_handle': str(screenName),
    					'image_location': str(image),
    					'tag': str(tag)
					}
					result = image_tags.insert_one(image_tag_data)
				imageCounter+=1
			except:
				imageCounter+=1

		print('Data stored in local MongoDB Atlas Cluster!')
	except:
		print(sys.exc_info())
		print('MongoDB Module Error!')
	return

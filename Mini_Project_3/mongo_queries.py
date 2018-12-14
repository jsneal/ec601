from pymongo import MongoClient
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
import sys
from bson.son import SON
"""
Based on code from: https://www.mongodb.com/blog/post/getting-started-with-python-and-mongodb
Info on aggregation in MongoDB gathered from: http://api.mongodb.com/python/current/examples/aggregation.html
"""
def mongo_queries():
	try:
		file = open('/home/jsneal/Desktop/API_Keys/MongoDB/password.txt', 'r') # The file where my API keys were stored.
		password = file.readline()
		mongoStr = 'mongodb://jsneal:'+ password +'@miniproject3-shard-00-00-ggtat.gcp.mongodb.net:27017,miniproject3-shard-00-01-ggtat.gcp.mongodb.net:27017,miniproject3-shard-00-02-ggtat.gcp.mongodb.net:27017/image_tags?ssl=true&replicaSet=MiniProject3-shard-0&authSource=admin&retryWrites=true'
		image_tagsClient = MongoClient(mongoStr)
		dbImage_tags = image_tagsClient.image_tags
		image_tags = dbImage_tags.image_tags

		result = image_tags.aggregate([
	    { "$group":  { "_id": "$tag", "count": { "$sum": 1 } } },
	    { "$sort": SON([("count", -1), ("_id", -1)])}
	    ])
		print(type(result))
		for one in result:
			queryStr = one['_id'] + ", " + str(one['count'])
			print(queryStr)
		
		print('MongoDB Query Successful!')
	except:
		print(sys.exc_info())
		print('MongoDB Query Error!')

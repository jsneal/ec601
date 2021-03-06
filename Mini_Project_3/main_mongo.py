"""
This is the top module for the MongoDB implementation of Mini_Project_3
This particular project reads the twitter statuses from a user selected twitter feed.
Then it gathers Google Vision's labels for these images by using their API.
Then it uses ffmpeg to turn these images into a slideshow video.
Make sure to create a directory for the Twitter images called Twitter_Pictures, or name it something else
and adjust the code in Twitter_API_Call.py.
Then it stores relevant information about the usage of this API to a MongoDB Atlas Cluster database.
"""
from Read_API_Keys import Read_API_Keys
from Twitter_API_Call import Twitter_API_Call
from Read_Gvis_API_Keys import Read_Gvis_API_Keys
from GoogleVis_API_Call import GoogleVis_API_Call
from Images_to_Video import Images_to_Video
from Clear_Twitter_Pictures_Folder import Clear_Twitter_Pictures_Folder
from signIn import signIn
from store_in_mongo import store_in_mongo
from mongo_queries import mongo_queries

[username, dateAccessed] = signIn() # outputs username used to call api
Clear_Twitter_Pictures_Folder()
print('Reading Twitter API keys . . .')
api_access_info = Read_API_Keys()
print('Twitter API keys retrieved!')
print('Calling Twitter API . . .')
[filename_list, screenName, image_url_list] = Twitter_API_Call(api_access_info) # outputs Twitter handle accessed
print('Images gathered from Twitter feed!')
print('Reading Google Vision API keys . . .')
credentials = Read_Gvis_API_Keys()
print('Google Vision API keys retrieved!')
print('Calling Google Vision API to retrieve labels . . . ')
[labels_per_image, image_list] = GoogleVis_API_Call(credentials, filename_list) # outputs labels per image as well as image names on computer in Twitter_Pictures folder
numOfImages = len(image_list) # records nyumber of images
print('Retrieved Google Vision''s labels for the Twitter Images!')
print('Assembling video from Twitter images . . .')
Images_to_Video()
print('Video assembled!')
print('\n\n')
print('API Mini Project completed! Watch Twitter_Video.avi with your favorite media player!')
print('Compare the images in the video with the labels from Google Vision listed earlier in the terminal output.')
print('Thanks for watching!')
store_in_mongo(username, dateAccessed, screenName, labels_per_image, image_url_list)
mongo_queries() # generates a query that shows how many instances of a certain tag have appeared in Twitter API accesses.



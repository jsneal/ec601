# Consulted documentation about python-twitter for the methods and class structure of twitter.api as well as pydoc twitter.api

## This module calls the Twitter API for Joan Cornella, grab's statuses from their Twitter timeline, 
## and prints the media of these statuses. 
## It is an initial file to get off the ground running with this project
import Read_API_Keys
import twitter
import requests
from io import BytesIO
from PIL import Image

""".request
with urllib.request.urlopen('') as response:
   html = response.read()"""
print(Read_API_Keys.api_key)
print(Read_API_Keys.api_secret_key)
print(Read_API_Keys.access_token)
print(Read_API_Keys.access_token_secret)
twitter_api = twitter.Api(consumer_key=Read_API_Keys.api_key,
                          consumer_secret=Read_API_Keys.api_secret_key,
                          access_token_key=Read_API_Keys.access_token,
                          access_token_secret=Read_API_Keys.access_token_secret)
print(twitter_api.VerifyCredentials())
print("\n\n\n")
sirjoancornella_statuses = twitter_api.GetUserTimeline(screen_name="sirjoancornella")
counter = 0
for status in sirjoancornella_statuses:
	if type(status.media) is list:
		print(status.media[0].media_url)
		response = requests.get(status.media[0].media_url) # from http://docs.python-requests.org/en/master/user/quickstart/#response-content
		img = Image.open(BytesIO(response.content))
img.show()
		


"""
	print(type(status.media))
	counter = counter+1
	print(counter)
	media_list = []
	tweet = []
	tweet.append(status.media)
	media_list.append(tweet)
print("---------------------------")
for tweets in media_list:
	for status in media_list:
		print(status[0])"""
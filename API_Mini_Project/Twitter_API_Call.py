# Consulted documentation about python-twitter for the methods and class structure of twitter.api as well as pydoc twitter.api

## This module calls the Twitter API for Joan Cornella, grab's statuses from their Twitter timeline, 
## and prints the media of these statuses. 
## It is an initial file to get off the ground running with this project
import twitter
import requests
from io import BytesIO
from PIL import Image

""".request
with urllib.request.urlopen('') as response:
   html = response.read()"""


twitter_api = twitter.Api(consumer_key='aq3WXwQGtK1NllOV0eXGhPfuY',
                          consumer_secret='7CNOFhFNdVZ6AOUZDCc6C2aaiiMZGLnmU34PgfMZwwdQnHUwTf',
                          access_token_key='1039252761295110145-15GbsAUmdsTasi3rt1QEYbpAg23ys5',
                          access_token_secret='iZv9jFSUXPe2tRgkyh9bD6MxAoCEsBFGaf8jRw3AhsipO')
print(twitter_api.VerifyCredentials())
print("\n\n\n")
sirjoancornella_statuses = twitter_api.GetUserTimeline(screen_name="sirjoancornella")
counter = 0
for status in sirjoancornella_statuses:
	if type(status.media) is list:
		print(status.media[0].display_url)

"""		response = requests.get(status.media[0].url)
		img = Image.open(BytesIO(response.content))
		print(type(img))"""
		


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
# Consulted documentation about python-twitter for the methods and class structure of twitter.api as well as pydoc twitter.api

## This module calls the Twitter API for Joan Cornella, grab's statuses from their Twitter timeline, 
## and prints the media of these statuses. 
## It is an initial file to get off the ground running with this project
import twitter

twitter_api = twitter.Api(consumer_key='aq3WXwQGtK1NllOV0eXGhPfuY',
                          consumer_secret='7CNOFhFNdVZ6AOUZDCc6C2aaiiMZGLnmU34PgfMZwwdQnHUwTf',
                          access_token_key='1039252761295110145-15GbsAUmdsTasi3rt1QEYbpAg23ys5',
                          access_token_secret='iZv9jFSUXPe2tRgkyh9bD6MxAoCEsBFGaf8jRw3AhsipO')
print(twitter_api.VerifyCredentials())
print("\n\n\n")
sirjoancornella_statuses = twitter_api.GetUserTimeline(screen_name="sirjoancornella")
for status in sirjoancornella_statuses:
	media_List = []
	medialist.append(status.media)
	print(status.media)
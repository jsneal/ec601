# Consulted documentation about python-twitter for the methods and class structure of twitter.api as well as pydoc twitter.api

## This module calls the Twitter API for Joan Cornella, grab's statuses from their Twitter timeline, 
## and prints the media of these statuses. 
## It is an initial file to get off the ground running with this project
def Twitter_API_Call(api_access_info):
    import twitter
    import urllib
    url_list = []
    api_key = api_access_info[0]
    api_secret_key = api_access_info[1]
    access_token = api_access_info[2]
    access_token_secret = api_access_info[3]
    twitter_api = twitter.Api(consumer_key=api_key,
                            consumer_secret=api_secret_key,
                            access_token_key=access_token,
                            access_token_secret=access_token_secret)
    sirjoancornella_statuses = twitter_api.GetUserTimeline(screen_name="sirjoancornella")
    counter = 0
    for status in sirjoancornella_statuses:
	    if type(status.media) is list:
		    print(status.media[0].media_url)
		    url_list.append(status.media[0].media_url)
		    print("\n")
            try:
                image_filename = "Twitter_Pictures/image"+str(counter)+".jpg"
                image = urllib.urlretrieve(status.media[0].media_url, image_filename)
                counter=counter+1
            except:
        	    counter=counter+1

# Consulted documentation about python-twitter for the methods and class structure of twitter.api as well as pydoc twitter.api

## This module calls the Twitter API for user entered Twitter Handle, grab's statuses from their Twitter timeline, 
## and prints the media of these statuses. 
def Twitter_API_Call(api_access_info):
    import twitter
    import urllib
    url_list = []
    filename_list = []
    api_key = api_access_info[0]
    api_secret_key = api_access_info[1]
    access_token = api_access_info[2]
    access_token_secret = api_access_info[3]
    twitter_api = twitter.Api(consumer_key=api_key,  # calling Twitter API
                            consumer_secret=api_secret_key,
                            access_token_key=access_token,
                            access_token_secret=access_token_secret)
    screenName = ""
    screenName = raw_input("Enter a twitter handle (without the @): ")
    screenName = "@" + screenName
    sirjoancornella_statuses = twitter_api.GetUserTimeline(screen_name=screenName)  # this gathers the twitter feed of @__screenName__ into a data structure
    zerostr = "-"
    digits = 0
    counter = 0
    for status in sirjoancornella_statuses:
	    if type(status.media) is list:
		    url_list.append(status.media[0].media_url)  # extracts the urls from the data structure gathered from twitterapi.GetUserTimeline()
            try:
                digits = counter/10
                zerostr = "-"+str(counter).rjust(3, "0")
                image_filename = "Twitter_Pictures/image"+zerostr+".jpg" # create filenames of each image. 
                # If one desires to store the images in a folder labeled something other than Twitter images
                # here is the place to change it. Replace Twitter_Images with the name of your filepath.
                image = urllib.urlretrieve(status.media[0].media_url, image_filename) # gathers the image from the url
                # and stores it in the image_filename.
                counter=counter+1
                filename_list.append(image_filename) # This list will be useful when the video is created.
            except:
              print('Loading . . .')
            digits = 0
    return [filename_list, screenName]


\

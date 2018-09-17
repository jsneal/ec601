file = open('/home/jsneal/Desktop/API_Keys/Twitter/api.txt', 'r')
api_key = file.readline()[0:-1]
api_secret_key = file.readline()[0:-1]
access_token = file.readline()[0:-1]
access_token_secret = file.readline()
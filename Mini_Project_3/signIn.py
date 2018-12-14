def signIn():
	import datetime
	username = raw_input("Enter your username: ")
	return [username, str(datetime.datetime.now())]
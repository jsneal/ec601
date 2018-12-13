def signIn():
	import datetime
	username = raw_input("Enter your username: ")
	return [username, datetime.datetime.now()]
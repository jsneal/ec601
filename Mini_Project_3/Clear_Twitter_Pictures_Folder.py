
def Clear_Twitter_Pictures_Folder():
	import os
	os.system("rm -rf Twitter_Pictures && mkdir Twitter_Pictures")
	os.system("rm -rf Twitter_Video.avi")
	print("Cleared Twitter_Pictures folder . . .")
	return
from Read_API_Keys import Read_API_Keys
from Twitter_API_Call import Twitter_API_Call
from Read_Gvis_API_Keys import Read_Gvis_API_Keys
from GoogleVis_API_Call import GoogleVis_API_Call

api_access_info = Read_API_Keys()
filename_list = Twitter_API_Call(api_access_info)
credentials = Read_Gvis_API_Keys()
[label_list, image_list] = GoogleVis_API_Call(credentials, filename_list)


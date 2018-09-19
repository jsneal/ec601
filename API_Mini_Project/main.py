from Read_API_Keys import Read_API_Keys
from Twitter_API_Call import Twitter_API_Call
from Read_Gvis_API_Keys import Read_Gvis_API_Keys
from GoogleVis_API_Call import GoogleVis_API_Call

api_access_info = Read_API_Keys()
Twitter_API_Call(api_access_info)
client = Read_Gvis_API_Keys()
GoogleVis_API_Call(client)


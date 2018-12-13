# Extracts Google Vision API keys from .json file.
def Read_Gvis_API_Keys():
    from google.oauth2 import service_account       # From Google documentation https://google-auth.readthedocs.io/en/latest/user-guide.html#service-account-private-key-files
    credentials = service_account.Credentials.from_service_account_file(
    '/home/jsneal/Desktop/API_Keys/Google Cloud/Mini_Project_GVision_Keys.json') # Replace with the filepath of your .json file.
    return credentials
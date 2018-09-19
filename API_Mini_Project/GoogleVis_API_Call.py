# Code mainly from "Using the Client Library in Google Vision Documentation"
def GoogleVis_API_Call(credentials, filename_list):
    import io
    import os

    # Imports the Google Cloud client library
    from google.cloud import vision
    from google.cloud.vision import types

    from google.cloud import vision
    client = vision.ImageAnnotatorClient(
        credentials=credentials)
    for twitter_image in filename_list[1:-1]:
        # The name of the image file to annotate
        try:
            file_name = os.path.join(
                os.path.dirname(__file__),
                twitter_image)
            
            # Performs label detection on the image file
            response = client.annotate_image({
                'image': {'source': {'image_uri': twitter_image}},
                'features': [{'type': vision.enums.Feature.Type.FACE_DETECTION}],
                })
        except:
            print('Error')
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

            # Loads the image into memory
            with io.open(file_name, 'rb') as image_file:
                content = image_file.read()

            image = types.Image(content=content)

            # Performs label detection on the image file
            response = client.label_detection(image=image)
            labels = response.label_annotations

            print('Labels:')
            for label in labels:
                print(label.description)
            print("\n\n")
        except:
            print('Error')
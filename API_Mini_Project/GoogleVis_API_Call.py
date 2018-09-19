# Code mainly from "Using the Client Library in Google Vision Documentation"
def GoogleVis_API_Call(credentials):
    import io
    import os

    # Imports the Google Cloud client library
    from google.cloud import vision
    from google.cloud.vision import types

    from google.cloud import vision
    client = vision.ImageAnnotatorClient(
        credentials=credentials)

    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        'Twitter_Pictures/image0.jpg')

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
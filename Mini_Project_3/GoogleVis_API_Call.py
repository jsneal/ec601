# Code and most comments mainly from "Using the Client Library in Google Vision Documentation"
def GoogleVis_API_Call(credentials, filename_list):
    import io
    import os
    label_list = []
    image_list = []
    labels_per_image = []
    # Imports the Google Cloud client library
    from google.cloud import vision
    from google.cloud.vision import types

    from google.cloud import vision
    labelstr = 'Labels for image '
    counter = 1
    try: # Calling the Google Vision API
        client = vision.ImageAnnotatorClient(
            credentials=credentials)
    except:
        print('Google Vision API call error')
    for twitter_image in filename_list[1:-1]:
        # The name of the image file to annotate
        try:
            file_name = os.path.join(
                os.path.dirname(__file__),
                twitter_image)
            image_list.append(file_name)
            # Loads the image into memory
            with io.open(file_name, 'rb') as image_file:
                content = image_file.read()

            image = types.Image(content=content)

            # Performs label detection on the image file
            response = client.label_detection(image=image)
            labels = response.label_annotations

            newlabelstr = labelstr + str(counter)
            print(newlabelstr) # Correspond labels with the order of images in video
            for label in labels:
                print(label.description)
                label_list.append(label.description)
            print("\n\n")
            labels_per_image.append(label_list)
            label_list = []
        except:
            print('Error detecting labels')     # In case label detection does not work
            label_list.append('No label')
            labels_per_image.append([])
        counter = counter+1
    return [labels_per_image, image_list]
"""
This module turns the collection of Twitter feed images into a slideshow.
os.system is used to operate commands from the bash command line.
"""
def Images_to_Video():
    import os
    # This framerate shows an image every ten seconds.
    # Be sure to adjust the filepath to whatever the folder is storing your images.
    os.system("ffmpeg -framerate 1/10 -pattern_type glob -i 'Twitter_Pictures/*.jpg' -pix_fmt yuv420p Twitter.avi")
    print("See earlier entries in the terminal for Google Vision's labels for the images in the video!")
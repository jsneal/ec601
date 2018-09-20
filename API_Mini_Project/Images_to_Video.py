def Images_to_Video():
    import os
    os.system("ffmpeg -framerate 1/10 -pattern_type glob -i 'Twitter_Pictures/*.jpg' -pix_fmt yuv420p out.avi")
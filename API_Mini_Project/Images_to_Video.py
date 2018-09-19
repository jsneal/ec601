
from ffmpy import FFmpeg

ff = FFmpeg(
    inputs={'input.ts': None},
    outputs={'output.mp4': None}
    )
ff.cmd
'ffmpeg -i input.ts output.mp4'
ff.run()
ffmpeg -f image2 -pattern_type glob -framerate 12 -i 'Twitter_Pictures/image*.jpeg' -s WxH image.avi
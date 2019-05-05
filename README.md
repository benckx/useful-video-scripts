### Required packages

* ffmpeg
* mencoder

### Cut videos in pieces

Cut a video in pieces of 30 seconds starting at 10 seconds. Flag `reencode` is optional
(I'm going to add an option for re-encoding to *.mov very soon).

`python3 cuts_in_pieces.py /home/user/video.mp4 --length 30 --offset 10 --reencode`
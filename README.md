## Required packages

* ffmpeg
* mencoder

## Add bin to the path

If you want to be able to use the tool from your terminal and from any location, 
add the following line at the end of your `.bashrc` or you `.zshrc` 
(change the location to match the location where you downloaded this repository):

    export PATH=$PATH:~/projects/useful-video-scripts

## Usage

### Cut a video in pieces

Cut a video in pieces of 30 seconds starting at 10 seconds:

    python3 videocuts.py --i /home/user/video.mp4 --length 30 --offset 10 --reencode mov

Or with the bin:

    videocuts --i video.mp4 --length 30 --offset 10 --reencode mov

#### Parameters

- Parameter `length` is mandatory (`60` by default)
- Parameter `offset` is optional (`0` by default)
- Parameter `reencode` is optional (`mp4` or `mov`)

## Required packages

* ffmpeg
* mencoder

### Installation

    sudo apt install ffmpeg mencoder

## Add to PATH

It's possible to use the scripts from the terminal by adding the following line 
at the end of `.bashrc` or `.zshrc`  (change the location to match the location 
where you downloaded this repository):

    export PATH=$PATH:~/projects/useful-video-scripts/bin

## Usage

### Cut a video in pieces

Cut a video in pieces of 30 seconds starting at 10 seconds:

    videocuts --i video.mp4 --length 30 --offset 10 --reencode mov

Or in Python:

    python3 videocuts.py --i /home/user/video.mp4 --length 30 --offset 10 --reencode mov

#### Parameters

- Parameter `length` is mandatory (`60` by default)
- Parameter `offset` is optional (`0` by default)
- Parameter `reencode` is optional (`mp4` or `mov`)

## Required packages

* ffmpeg
* mencoder


    sudo apt install ffmpeg mencoder

## Add to PATH

It's possible to use the scripts from the terminal by adding the following line 
at the end of `.bashrc` or `.zshrc`  (change the location to match the location 
where you downloaded this repository):

    export PATH=$PATH:~/projects/useful-video-scripts/bin

## Usage

### Cut in pieces

Cut a video in pieces of 30 seconds starting at 10 seconds:

    videocuts video.mp4 --length 30 --offset 10 --reencode mov

Or in Python:

    python3 videocuts.py /home/user/video.mp4 --length 30 --offset 10 --reencode mov

#### Parameters

- `length` is optional (`60` by default)
- `offset` is optional (`0` by default)
- `reencode` is optional (`mp4` or `mov`)

### Compress

    videocompress video.mp4 --crf 23

#### Parameters

- `crf` is the quality. According to [ffmpeg](https://trac.ffmpeg.org/wiki/Encode/H.264): 
"_The range of the Constant Rate Factor (CRF) scale is 0–51, where 0 is lossless, 23 is 
the default, and 51 is worst quality possible. A lower value generally leads to higher 
quality, and a subjectively sane range is 17–28. Consider 17 or 18 to be visually lossless 
or nearly so; it should look the same or nearly the same as the input but it isn't technically lossless._"

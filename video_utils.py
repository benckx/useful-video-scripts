import os
import subprocess

import math


def get_video_duration_seconds(file_name):
  command = "ffmpeg -i " + file_name + " 2>&1 | grep Duration | cut -d ' ' -f 4 | sed s/,//"
  result = subprocess.run(command, shell=True, stdout=subprocess.PIPE)
  duration = result.stdout.decode("utf-8")
  split = duration.replace('.', ':').split(':')
  minutes = int(split[1])
  seconds = int(split[2])
  return seconds + (60 * minutes)


def seconds_to_timestamp(seconds: int):
  minutes = math.floor(seconds / 60)
  seconds = seconds - (60 * minutes)

  minutes_padded = str(minutes).rjust(2, '0')
  seconds_padded = str(seconds).rjust(2, '0')

  return '00:' + minutes_padded + ':' + seconds_padded


def re_encode_video(input_file, output_file, encoding_format):
  encoding = None

  if encoding_format == 'mp4':
    encoding = '-c:v libx264 -profile:v high -crf 17 -pix_fmt yuv420p'
  elif encoding_format == 'mov':
    encoding = '-acodec copy -vcodec copy -f mov'
  else:
    exit(1)

  re_encode_command = 'ffmpeg -i ' + input_file + ' ' + encoding + ' ' + output_file
  subprocess.run(re_encode_command, shell=True)
  os.remove(input_file)

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
    encoding = '-c:v libx264 -crf 17 -pix_fmt yuv420p'
  elif encoding_format == 'mov':
    encoding = '-acodec copy -vcodec copy -f mov'
  else:
    exit(1)

  command = 'ffmpeg -i ' + input_file + ' ' + encoding + ' ' + output_file
  print(command)
  subprocess.run(command, shell=True)
  os.remove(input_file)


def extract_video(input_file, output_file, length, offset):
  ss = seconds_to_timestamp(offset)
  endpos = seconds_to_timestamp(length)
  command = 'mencoder -ss ' + ss + ' -endpos ' + endpos + ' -oac copy -ovc copy ' + input_file + ' -o ' + output_file
  print(command)
  subprocess.run(command, shell=True)


def reverse_video(input_file, output_file):
  command = 'ffmpeg -i {} -c:v libx264 -crf 17 -pix_fmt yuv420p -vf reverse {}'.format(input_file, output_file)
  print(command)
  subprocess.run(command, shell=True)


def merge_videos(input1, input2, output_file):
  command = 'mencoder -oac copy -ovc copy ' + input1 + ' ' + input2 + ' -o ' + output_file
  print(command)
  subprocess.run(command, shell=True)

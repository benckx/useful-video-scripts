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

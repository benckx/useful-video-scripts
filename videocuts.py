import os
import subprocess

import math

from param_utils import get_param_int, get_param_str
from video_utils import seconds_to_timestamp, get_video_duration_seconds


def main():
  input_file = get_param_str('i', default=None)
  length = get_param_int('length', default=60)
  offset = get_param_int('offset', default=0)
  re_encode = get_param_str('reencode', default=None)

  print('input file -> {}'.format(input_file))
  print('length -> {} sec.'.format(length))
  print('offset -> {} sec.'.format(offset))
  print('re_encode -> {}'.format(re_encode))

  if input_file is None:
    print('input file parameter is mandatory')
    exit(1)

  if re_encode is not None and re_encode != "mp4" and re_encode != "mov":
    print('reencode format {} not known'.format(re_encode))
    exit(1)

  file_name = input_file.split('/')[-1]
  file_folder = input_file[0:input_file.find(file_name)]
  file_name_no_extension = file_name.split('.')[0]
  duration = get_video_duration_seconds(input_file)
  endpos = seconds_to_timestamp(length)
  nbr_of_bits = math.floor((duration - offset) / length)

  print('length: {}'.format(length))
  print('offset: {}'.format(offset))
  print(input_file)
  print(file_name)
  print(file_name_no_extension)
  print(file_folder)
  print(duration)
  print(nbr_of_bits)

  count = 1
  for i in range(nbr_of_bits):
    start = (i * length) + offset
    end = ((i + 1) * length) + offset
    print("bit {} --> from {} to {}".format(i, start, end))
    count += 1

  count = 1
  for i in range(nbr_of_bits):
    ss = seconds_to_timestamp((i * length) + offset)
    cut_num = str(count).rjust(3, '0')
    count += 1
    output_file = file_folder + file_name_no_extension + '_' + cut_num + '.mp4'
    command = 'mencoder -ss ' + ss + ' -endpos ' + endpos + ' -oac copy -ovc copy ' + input_file + ' -o ' + output_file
    subprocess.run(command, shell=True)

    if re_encode is not None:
      re_encode_output_file = None
      encoding = None

      if re_encode == 'mp4':
        re_encode_output_file = file_folder + file_name_no_extension + '_' + cut_num + '_encoded' + '.mp4'
        encoding = '-c:v libx264 -profile:v high -crf 17 -pix_fmt yuv420p'
      elif re_encode == 'mov':
        re_encode_output_file = file_folder + file_name_no_extension + '_' + cut_num + '_encoded' + '.mov'
        encoding = '-acodec copy -vcodec copy -f mov'

      if re_encode_output_file is None or encoding is None:
        exit(1)

      re_encode_command = 'ffmpeg -i ' + output_file + ' ' + encoding + ' ' + re_encode_output_file
      subprocess.run(re_encode_command, shell=True)
      os.remove(output_file)


if __name__ == "__main__":
  main()

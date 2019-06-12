import os

from param_utils import get_param_int, get_param_str, get_input_file
from video_utils import extract_video, reverse_video, merge_videos, re_encode_video


def extract(input_file, length, offset):
  input_file_no_extension = input_file.split('.')[0]
  input_file_extension = input_file.split('.')[1]

  input_file_extract = input_file_no_extension + "_extract." + input_file_extension
  extract_video(input_file, input_file_extract, length, offset)

  re_encoded_output_file = input_file_no_extension + "_extract_re_encoded." + input_file_extension
  re_encode_video(input_file_extract, re_encoded_output_file, 'mp4')

  files_to_delete.append(input_file_extract)

  return re_encoded_output_file


def reverse(input_file):
  input_file_no_extension = input_file.split('.')[0]
  input_file_extension = input_file.split('.')[1]

  reversed_output_file = input_file_no_extension + '_reverse.' + input_file_extension
  reverse_video(input_file, reversed_output_file)
  return reversed_output_file


def main():
  input_file = get_input_file()
  length = get_param_int('length', default=None)
  offset = get_param_int('offset', default=0)
  re_encode_format = get_param_str('reencode', default=None)

  if input_file is None:
    print('input file parameter is mandatory')
    exit(1)

  if re_encode_format is not None and re_encode_format != "mp4" and re_encode_format != "mov":
    print('reencode format {} not known'.format(re_encode_format))
    exit(1)

  file_name = input_file.split('/')[-1]
  file_name_no_extension = file_name.split('.')[0]
  file_extension = file_name.split('.')[1]

  if length is not None:
    loop_part01 = extract(input_file, length, offset)
  else:
    loop_part01 = input_file

  loop_part02 = reverse(loop_part01)

  output_loop_file = file_name_no_extension + "_loop01." + file_extension
  merge_videos(loop_part01, loop_part02, output_loop_file)

  if length is not None:
    files_to_delete.append(loop_part01)

  files_to_delete.append(loop_part02)


if __name__ == "__main__":
  files_to_delete = []
  main()
  for file in files_to_delete:
    os.remove(file)

import os

from param_utils import get_param_int, get_param_str, get_input_file
from video_utils import extract_video, reverse_video, merge_videos, re_encode_video


def main():
  input_file = get_input_file()
  length = get_param_int('length', default=None)
  offset = get_param_int('offset', default=None)
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

  if length is not None and offset is not None:
    output_file_extract = file_name_no_extension + "_extract." + file_extension
    re_encoded_extract_output_file = file_name_no_extension + "_extract_re_encoded." + file_extension
    extract_video(input_file, output_file_extract, length, offset)
    re_encode_video(output_file_extract, re_encoded_extract_output_file, 'mp4')
    input_file = re_encoded_extract_output_file
    file_name_no_extension = file_name_no_extension + "_extract_re_encoded"
    files_to_delete.append(output_file_extract)
    files_to_delete.append(input_file)

  reversed_output_file = file_name_no_extension + '_reverse.' + file_extension
  reverse_video(input_file, reversed_output_file)
  loop_file = file_name_no_extension + '_loop.' + file_extension
  merge_videos(input_file, reversed_output_file, loop_file)
  files_to_delete.append(reversed_output_file)

  for file in files_to_delete:
    os.remove(file)

if __name__ == "__main__":
  files_to_delete = []
  main()

import math

from param_utils import get_param_int, get_param_str, get_input_file
from video_utils import get_video_duration_seconds, re_encode_video, extract_video


def main():
  input_file = get_input_file()
  length = get_param_int('length', default=60)
  offset = get_param_int('offset', default=0)
  re_encode_format = get_param_str('reencode', default=None)

  if input_file is None:
    print('input file parameter is mandatory')
    exit(1)

  if re_encode_format is not None and re_encode_format != "mp4" and re_encode_format != "mov":
    print('reencode format {} not known'.format(re_encode_format))
    exit(1)

  file_name = input_file.split('/')[-1]
  file_folder = input_file[0:input_file.find(file_name)]
  file_name_no_extension = file_name.split('.')[0]
  duration = get_video_duration_seconds(input_file)
  nbr_of_bits = math.floor((duration - offset) / length)

  count = 1
  for i in range(nbr_of_bits):
    start = (i * length) + offset
    end = ((i + 1) * length) + offset
    print("bit {} --> from {} to {}".format(i, start, end))
    count += 1

  count = 1
  for i in range(nbr_of_bits):
    cut_num = str(count).rjust(3, '0')
    output_file = file_folder + file_name_no_extension + '_' + cut_num + '.mp4'
    extract_video(input_file, output_file, length, (i * length) + offset)
    count += 1

    if re_encode_format is not None:
      re_encode_output_file = None

      if re_encode_format == 'mp4':
        re_encode_output_file = file_folder + file_name_no_extension + '_' + cut_num + '_encoded.mp4'
      elif re_encode_format == 'mov':
        re_encode_output_file = file_folder + file_name_no_extension + '_' + cut_num + '_encoded.mov'
      else:
        exit(1)

      re_encode_video(output_file, re_encode_output_file, re_encode_format)


if __name__ == "__main__":
  main()

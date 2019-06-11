import subprocess

from param_utils import get_param_int, get_param_str


def main():
  input_file = get_param_str('i', default=None)
  crf = get_param_int('crf', default=25)

  print('input file == {}'.format(input_file))
  print('crf == {} sec.'.format(crf))

  if input_file is None or crf is None:
    print('i and crf parameters are mandatory')
    exit(1)

  file_name = input_file.split('/')[-1]
  file_name_no_extension = file_name.split('.')[0]
  file_extension = file_name.split('.')[1]
  output_file = '{}_crf{}.{}'.format(file_name_no_extension, crf, file_extension)

  command = 'ffmpeg -i {} -c:v libx264 -crf {} -pix_fmt yuv420p {}'.format(input_file, crf, output_file)
  print(command)
  subprocess.run(command, shell=True)


if __name__ == "__main__":
  main()

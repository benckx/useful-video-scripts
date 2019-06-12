import sys


def get_input_file():
  input_file = get_param_str('i', default=None)
  if input_file is None:
    first_arg = sys.argv[1]
    if not first_arg.startswith('--'):
      return first_arg
  else:
    return input_file

  return None


def get_param_str(key, default=None):
  result = get_param(key)
  if result is None:
    print('use default value for {} -> {}'.format(key, default))
    return default
  else:
    return result


def get_param_int(key, default=None):
  result = get_param(key)
  if result is None:
    print('use default value for {} -> {}'.format(key, default))
    return default
  else:
    return int(result)


def get_param(key):
  if len(sys.argv) > 1:
    params = sys.argv[0:]
    for idx, param in enumerate(params):
      if param == '--' + key:
        value = params[idx + 1]
        print('{} -> {}'.format(key, value))
        return value

  return None

def reverse_string(s):
  pass # todo
  if len(s) == 0:
    return ""
  chars = list(s)
  return chars.pop() + reverse_string(chars)
def last2(str):
  c = 0
  x = 0
  while x < len(str)-2:
    if str[x:x+2] == str[-2:]:
      c += 1
    x += 1
  return c

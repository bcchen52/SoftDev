def string_bits(str):
  k = True
  new = ""
  for i in str:
    if k:
      new += i
    k = not k
  return new

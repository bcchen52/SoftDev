def front3(str):
  yehaw = []
  str2 = ""
  while len(yehaw) < 3:
    yehaw.append(str[:3])
  for yee in yehaw:
    str2 += yee
  return str2

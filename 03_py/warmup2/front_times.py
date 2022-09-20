def front_times(str, n):
  k=""
  m=0
  while m<n:
    if len(str) < 3:
      k += str
    else:
      k += str[0:3]
    m+=1
  return k

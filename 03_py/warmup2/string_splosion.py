def string_splosion(str):
  k,x = "",0
  for i in str:
    k += str[:x+1]
    x += 1
  return k

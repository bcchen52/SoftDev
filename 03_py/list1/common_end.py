def common_end(a, b):
  return(a[0]==b[0] or a[-1]==b[-1])

#t1 = [[1,2,3],[7,3]]
t1 = [[1,2,3],[7,3,2]]
#t1 = [[1,2,3],[1,3]]
#comment out different test cases

print(f"common_end([{','.join(str(x) for x in t1[0])}],[{','.join(str(x) for x in t1[1])}]) is {str(common_end(t1[0],t1[1]))}")
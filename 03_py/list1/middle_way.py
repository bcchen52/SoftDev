def middle_way(a, b):
  new = []
  new.append(a[1])
  new.append(b[1])
  return(new)

t1 = [[1,2,3],[4,5,6]]
#t1 = [[7,7,7],[3,8,0]]
#t1 = [[5,2,9],[1,4,5]]

print(f"middle_way([{','.join(str(x) for x in t1[0])}],[{','.join(str(x) for x in t1[1])}]) is {str(middle_way(t1[0],t1[1]))}")


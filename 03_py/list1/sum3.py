def sum3(nums):
  tot = 0
  for i in nums:
    tot += i
  return(tot)

t1 = [1,2,3]
#t1 = [5,11,2]
#t1 = [7,0,0]
print(f"sum3([{','.join(str(x) for x in t1)}]) is {str(sum3(t1))}")

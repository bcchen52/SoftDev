def sum3(nums):
  tot = 0
  for i in nums:
    tot += i
  return(tot)

t1 = [1,2,3]
t2 = [5,11,2]
t3 = [7,0,0]
print(f"sum3([{','.join(str(x) for x in t1)}]) is {str(sum3(t1))}")
print(f"sum3([{','.join(str(x) for x in t2)}]) is {str(sum3(t2))}")
print(f"sum3([{','.join(str(x) for x in t3)}]) is {str(sum3(t3))}")
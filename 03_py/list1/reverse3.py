def reverse3(nums):
  nums.reverse()
  return(nums)

t1 = [1,2,3]
#t1 = [5,11,9]
#t1 = [7,0,0]

print(f"reverse3([{','.join(str(x) for x in t1)}]) is {str(reverse3(t1))}")
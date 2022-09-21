def sum2(nums):
  k = len(nums)
  if k > 1:
    return(nums[0]+nums[1])
  if k == 1:
    return(nums[0])
  if k == 0:
    return(0)

t1 = [1,2,3]
#t1 = [1,1]
#t1 = [1,1,1,1]

print(f"sum2([{','.join(str(x) for x in t1)}]) is {str(sum2(t1))}")
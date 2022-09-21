def max_end3(nums):
  k = 0
  high = nums[0]
  if nums[-1] > high:
    high = nums[-1]
  while k < 3:
    nums[k] = high
    k += 1
  return(nums)

t1 = [1,2,3]
#t1 = [11,5,9]
#t1 = [2,11,3]

print(f"max_end3([{','.join(str(x) for x in t1)}]) is {str(max_end3(t1))}")

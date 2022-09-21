def max_end3(nums):
  k = 0
  high = nums[0]
  if nums[-1] > high:
    high = nums[-1]
  while k < 3:
    nums[k] = high
    k += 1
  return(nums)

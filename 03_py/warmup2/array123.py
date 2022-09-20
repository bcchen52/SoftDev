def array123(nums):
  k = 0
  for x in nums:
    if x == 3:
      if nums[k-1] == 2 and nums[k-2] == 1:
        return True
    k += 1
  return False

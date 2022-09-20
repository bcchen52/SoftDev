def array_front9(nums):
  k = 0
  for x in nums:
    if x == 9 and k < 4:
      return True
    k += 1
  return False

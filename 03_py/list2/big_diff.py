def big_diff(nums):
  big = 0
  smol = 0 
  done = False
  for i in nums:
    if i > big:
      big = i
      if done == False:
        smol = i
        done =True
    if i < smol:
      smol = i
  return(big-smol)

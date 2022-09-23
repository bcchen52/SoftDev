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

t1 = [10,3,5,6]
#t1 = [7,2,10,9]
#t1 = [2,10,7,2]

print(f"big_diff([{','.join(str(x) for x in t1)}]) is {str(big_diff(t1))}")
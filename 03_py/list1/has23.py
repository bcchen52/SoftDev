def has23(nums):
  return(nums[0]==2 or nums[0]==3 or nums[1]==2 or nums[1]==3)

t1 = [2,5]
#t1 = [4,3]
#t1 = [7,5]

print(f"has23([{','.join(str(x) for x in t1)}]) is {str(has23(t1))}")

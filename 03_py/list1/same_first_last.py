def same_first_last(nums):
  return(len(nums)>0 and nums[0]==nums[-1])

t1 = [1,2,3]
#t1 = [1,2,3,1]
#t1 = [1,2,1]

print(f"same_first_last([{','.join(str(x) for x in t1)}]) is {str(same_first_last(t1))}")

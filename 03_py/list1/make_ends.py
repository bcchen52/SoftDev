def make_ends(nums):
  new = []
  new.append(nums[0])
  new.append(nums[-1])
  return(new)

t1 = [1,2,3]
#t1 = [1,2,3,4]
#t1 = [7,4,6,2]

print(f"make_ends([{','.join(str(x) for x in t1)}]) is {str(make_ends(t1))}")
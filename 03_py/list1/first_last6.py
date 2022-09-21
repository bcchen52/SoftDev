def first_last6(nums):
  fir = nums[0] 
  las = nums[-1]
  return(fir == 6 or las == 6)

t1 = [1,2,6]
#t1 = [6,1,2,3]
#t1 = [13,6,1,2,3]

print(f"first_last6([{','.join(str(x) for x in t1)}]) is {str(first_last6(t1))}")

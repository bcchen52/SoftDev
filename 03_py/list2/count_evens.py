def count_evens(nums):
  return sum(i%2==0 for i in nums)

t1 = [2, 1, 2, 3, 4]
#t1 = [2, 2, 0]
#t1 = [1, 3, 5]

print(f"count_evens([{','.join(str(x) for x in t1)}]) is {str(count_evens(t1))}")
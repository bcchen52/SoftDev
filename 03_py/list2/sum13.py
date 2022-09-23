def sum13(nums):
    math = 0
    prev = 0
    thirt = False
    for i in range(len(nums)):
        math += nums[i]
        if nums[i] == 13 and prev != 13:
            math = math -13
        if prev == 13:
            math = math - nums[i]
        prev = nums[i]
    return(math)

t1 = [1,2,2,1]
#t1 = [1,1]
#t1 = [1,2,2,1,13]

print(f"sum13([{','.join(str(x) for x in t1)}]) is {str(sum13(t1))}")
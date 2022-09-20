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

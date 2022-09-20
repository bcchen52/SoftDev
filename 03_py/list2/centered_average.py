def centered_average(nums):
    nums.sort()
    new = nums[1:-1]
    total = 0
    t = 0
    for i in new:
        total = total + i
        t += 1
    return(total//(t))

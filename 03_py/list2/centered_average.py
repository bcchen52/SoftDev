def centered_average(nums):
    nums.sort()
    new = nums[1:-1]
    total = 0
    t = 0
    for i in new:
        total = total + i
        t += 1
    return(total//(t))

#t1 = [1,2,3,4,100]
#t1 = [1,1,5,5,10,8,7]
t1 = [-10,-4,-2,-4,-2,0]

print(f"centered_average([{','.join(str(x) for x in t1)}]) is {str(centered_average(t1))}")
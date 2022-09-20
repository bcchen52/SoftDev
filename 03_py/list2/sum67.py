def sum67(nums):
    total = 0
    start = False
    for i in nums:
        if i == 6:
            start = True
        if start == False:
            total = total + i
        if start == True and i == 7:
            start = False
    return(total)

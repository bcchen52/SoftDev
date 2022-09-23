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

#t1 = [1,2,2]
t1 = [1,2,2,6,99,99,7]
#t1 = [1,1,6,7,2]

print(f"sum67([{','.join(str(x) for x in t1)}]) is {str(sum67(t1))}")
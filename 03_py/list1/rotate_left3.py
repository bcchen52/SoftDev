def rotate_left3(nums):
    nums2 = nums
    back = nums.pop(0)
    nums.append(back)
    return(nums)

t1 = [1,2,3]
#t1 = [5,11,9]
#t1 = [7,0,0]

print(f"rotate_left3([{','.join(str(x) for x in t1)}]) is {str(rotate_left3(t1))}")

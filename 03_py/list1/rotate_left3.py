def rotate_left3(nums):
    nums2 = nums
    back = nums.pop(0)
    nums.append(back)
    return(nums)

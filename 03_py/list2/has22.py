def has22(nums):
    first_con = False
    second_con = False
    ticker = 0
    for i in nums:
        ticker = ticker-1
        if i == 2:
            if first_con == False:
                first_con = True
                ticker = 2
            if first_con == True and ticker == 1:
                second_con = True
        else:
          if ticker == 1:
            first_con = False
          
    return(second_con)

t1 = [1,2,2]
#t1 = [1, 2, 1, 2]
#t1 = [2,1,2]

print(f"has22([{','.join(str(x) for x in t1)}]) is {str(has22(t1))}")
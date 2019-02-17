# 2 ary of ints, find 2 closeest number from 1st and 2nd ary  

# 1. sort both ary
# 2. l , r pointers at start of arys
    # for every pair of l r vals, compute diff
    #     if diff < , move left,
    #     if diff >, move right,
    #     if diff == 0, return
# O(nlg(n) + mlg(m))  

def smallestDifference(ary1, ary2):
    #sorts in place 
    ary1.sort()
    ary2.sort()
    

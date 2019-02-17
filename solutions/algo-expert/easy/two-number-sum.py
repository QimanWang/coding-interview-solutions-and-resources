# ary = [3,5,11,1,4,-1]    tgt =10

#given: unique, not sorted,
'''
for each num:
    calc compliment = tgt - num in set,
    
    if in set, return pair,remove compliment
    else we put num in set

time:O(n) space: O(n) b/c store each val

'''
def twoSum(nums,tgt):
    s = set()
    res=[]
    
    for num in nums:
        diff = tgt - num
        if diff in s:
            res.append([num,tgt-num]) 
            s.remove(diff)
        else:
            s.add(num)    
    return res

ary = [3,5,10,0,-1,11] 
tgt =10

print(twoSum(ary,tgt))

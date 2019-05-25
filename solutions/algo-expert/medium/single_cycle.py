ary = [2,3,1,-4,-4,2]


'''
each node is visited once before returning to starting node
return has cycle,
else return false
'''
def hasSingleCycle(ary):
    len_ary= len(ary)
    movesLeft = len(ary)
    curr_idx = 0
    
    # while has more moves
    while movesLeft > 0:
        # how much to move?
        step = ary[curr_idx%len_ary]
        temp_idx = curr_idx
        # % len(ary) to wrap arpund
        curr_idx = (curr_idx+step) % len_ary

        if temp_idx == curr_idx:
            return False
        # print(curr_idx)
        movesLeft-=1
    
    return True if curr_idx ==0 else False

ary1 = [0,1,1,1,1]
print(hasSingleCycle(ary1))

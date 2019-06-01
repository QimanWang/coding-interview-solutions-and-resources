'''
some kind of bst steps


'''
def searchForRange(array, target):
    
     # final result
    final_range = [-1,-1]

    alteredBst(array,target,0,len(array)-1, final_range,True)
    alteredBst(array,target,0,len(array)-1, final_range,False)

    return final_range

def alteredBst(ary,tgt,l,r,finalRange,goLeft):

    # iteratively traversing the ary
    while l <= r:
        m = (l + r)//2
        # if smaller than tgt, we need to go right
        if ary[m]< tgt:
            l = m+1
        # if bigger than tgt, we need to go left
        elif ary[m]> tgt:
            r = m-1
        else:
            if goLeft:
                if m == 0 or ary[m-1] != tgt:
                    finalRange[0] = m
                    return 
                else:
                    r=m-1
            else:
                if m == len(ary)-1 or ary[m+1] != tgt:
                    finalRange[1] = m
                    return 
                else:
                    l = m+1
    # return finalRange
        
        





ary = [0,1,21,33,45,45,45,45,45,45,61,71,71]
tgt = 45

print(searchForRange(ary,tgt))


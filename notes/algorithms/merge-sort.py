'''
merge sort :
input: [3,2,1]
[3,2] | [1]
[3] [2] | [1]

merge([3],[2]):
[2,3]

merge([2,3],1)

[1,2,3]
'''

def merge_sort(lst):
    
    # check if smallest unit, if not we keep breaking up
    if len(lst) >1:
        mid_idx = (len(lst)-1)//2
        print('mid_idx: ',mid_idx)
        l = merge_sort(lst[:mid_idx+1])
        r = merge_sort(lst[mid_idx+1:])
        return merge(l,r)
    else :
        return lst


def merge(listL,listR):
    res = []
    i,j = 0,0
    # while there's stuff in both list
    while i < len(listL)  and j < len(listR):
        if listL[i] < listR[j]:
            res.append(listL[i])
            i+=1
        else:
            res.append(listR[j])
            j+=1
    
    while i < len(listL):
        res.append(listL[i])
        i+=1
    while j < len(listR):
        res.append(listR[j])
        j+=1
    return res








lst = [1,4,39,2,1]
res = merge_sort(lst)
print(res)

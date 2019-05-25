'''
top ancestor is the root node. we start traversing from this node.
we can do a dfs and stop once we hit descentdent one, then another to find descendent 2
then we compare the paths and find the first common node.



time: O(d) where d is the lowest descent
space: O(1)

'''

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    # get depth difference and move lower depth to higher depth
    d1Depth = getDescendentDepth(descendantOne,topAncestor)
    d2Depth = getDescendentDepth(descendantTwo,topAncestor)

    # if not same depth, we move lower to higher
    if d1Depth > d2Depth:
        return backTrackTree(descendantOne,descendantTwo,d1Depth-d2Depth)
    else:
        return backTrackTree(descendantTwo,descendantOne,d2Depth-d1Depth)


def getDescendentDepth(descendent,ancestor):
    depth = 0
    while(descendent is not ancestor):
        depth+=1
        descendent=descendent.ancestor
    
    return depth

def backTrackTree(lower_d,higher_d, diff):
    while diff >0:
        lower_d=lower_d.ancestor
        diff -=1

    while lower_d != higher_d:
        lower_d = lower_d.ancestor
        higher_d = higher_d.ancestor

    return lower_d
    
    


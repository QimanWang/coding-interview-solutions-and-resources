'''
questions : valid bst? positive neg? unique solution?

thoughts:
we only need to care about the parent, left and right.
so we need to keep track of 3 digits at max O(1) space.
how do we bracket the 3 signicant values.
we can traverse using bfs, becasue we want to know neighbors and 
stop when we know it gets too large / small.

avg O(lg(n))
worst O(n) bc all new vals is bigger / smaller
'''

# recursive implementation
def findClosestValueInBst(tree, target):
    
    # Helper method
    return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):

    # base case when we reach leaf
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value

    if target < tree.value:
        return findClosestValueInBstHelper(tree.left, target, closest)

    elif target > tree.value:
        return findClosestValueInBstHelper(tree.right, target, closest)

    #equal
    else:
        return closest

# iterative implementation
def findClosestValueInBst(tree, target):
    
    # Helper method
    return findClosestValueInBstHelper(tree, target, float("inf"))

def findClosestValueInBstHelper(tree, target, closest):

    currNode = tree

    while currNode is not None:

        if abs(target - closest) > abs(target - currNode.value):
            closest = currNode.value

        if target < currNode.value:
            currNode = currNode.left

        elif target > currNode.value:
            currNode = currNode.right
        else:
            break
    return closest

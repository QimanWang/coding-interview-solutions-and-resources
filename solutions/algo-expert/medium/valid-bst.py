'''
bst has properties that left node is smaller than parent node,
right node is greater than parent node.
given a node, we need to check it's childrens recursively

note that there is a extra constraint, because the paren'ts parent is either the max/min the grandchild can be

if grandpa is 10, left child can be <10, left child's right has to be >left child and < grandpa

'''


def validateBst(tree):
    # Write your code here.
    return validateBstHelper(tree, float("-inf"), float("inf"))


def validateBstHelper(tree, minVal, maxVal):
    # we hit leaf
    if tree is None:
        return True
    if tree.value < minVal or tree.value >= maxVal:
        return False

    leftIsValid = validateBstHelper(tree.left, minVal, tree.value)
    rightIsValid = validateBstHelper(tree.right, tree.value, maxVal)

    return leftIsValid and rightIsValid

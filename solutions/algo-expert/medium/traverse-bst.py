'''
inorder: go as left as possible, then curr, then right
'''


def inOrderTraverse(tree, array):
    # Write your code here.
    if tree is None:
        return array
    inOrderTraverse(tree.left, array)
    array.append(tree.value)
    inOrderTraverse(tree.right, array)

    return array


def preOrderTraverse(tree, array):
    # Write your code here.
    pass


def postOrderTraverse(tree, array):
    # Write your code here.
    pass

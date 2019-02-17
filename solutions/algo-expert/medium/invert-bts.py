'''
we have to reverse the whole level
hmm, is there a good traversal way to do this?
for a simple case of n modes
n=1
curr = tree.value, no childs

n= 2 or 3
there is one child,
tmp = curr.left
curr.left = curr.right
curr.right = tmp

n = 3,4, ... level 2


'''


def invertBinaryTree(tree):
    # Write your code here.
    if tree is not None:
        swap(tree)
        invertBinaryTree(tree.left)
        invertBinaryTree(tree.right)


def swap(tree):
    tree.left, tree.right = tree.right, tree.left

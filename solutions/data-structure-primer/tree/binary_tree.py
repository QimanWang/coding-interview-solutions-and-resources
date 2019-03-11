'''
tree is structured vs linear like list/ array
      tree
      ----
       j    <-- root
     /   \
    f      k  
  /   \      \
 a     h      z    <-- leaves 

ex:
file system
-----------
     /    <-- root
  /      \
...       home
      /          \
   ugrad        course
    /       /      |     \
  ...      cs101  cs112  cs113  

faster search than list, but slower than list.
faster del/ins than array, but slower than list
not limited like list, arrays are limited in size

Main applications of trees include:
1. Manipulate hierarchical data.
2. Make information easy to search (see tree traversal).
3. Manipulate sorted lists of data.
4. As a workflow for compositing digital images for visual effects.
5. Router algorithms
6. Form of a multi-stage decision-making (see business chess).



# Binary Tree 
class Node: 

    # constructor
	def __init__(self,key): 
		self.left = None
		self.right = None
		self.val = key 

# create root 
root = Node(1) 

root.left	 = Node(2); 
root.right	 = Node(3); 
root.left.left = Node(4); 

              1 
            /	 \ 
            2	 3 
            / \	 / \ 
        4 None None None 
        / \ 
        None None

properties:
num of nodes at level i = 2^(i-1)
num of node total of height h = 2^h -1
height = ⌈ Log2(N+1) ⌉ -1 ,
A Binary Tree with L leaves has at least   ⌈ Log2L ⌉ + 1   levels   
n Binary tree where every node has 0 or 2 children, number of leaf nodes is always one more than nodes with two children.

types:
full bt:
every node has 2 child, except leave
             18
           /    \   
         15     20    
        /  \       
      40    50   
    /   \
   30   50

complete bt:
all level are filled except last,
and last level are filled from left to right first.
               18
           /       \  
         15         30  
        /  \        /  \
      40    50    100   40
     /  \   /
    8   7  9 

perfect:
full and complete

balanced: height no diff by 1
avl is balanced because level no diff by 1
red black is balaned

A degenerate (or pathological) tree:
A Tree where every internal node has one child
basically a linked list

'''

# define node the building block of trees
class Node():

    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None
    

if __name__ == '__main__': 
    root = Node(1)  
    root.left = Node(2)  
    root.left.left = Node(4)  
    root.right = Node(3)  
    root.right.left = Node(15)  
    root.right.right = Node(8)  

    print(root.value)
    print(root.left.value)
    print(root.right.value)


# let's find a better way to traverse the tree.
def inOrderTraversal(root):
    
    if root is N:





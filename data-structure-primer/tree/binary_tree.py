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

'''
BST methods:
insert()
delete()
'''


'''
Array implementation:
       A(0)    
     /   \
    B(1)  C(2)  
  /   \      \
 D(3)  E(4)   F(6) 
OR,
      A(1)    
     /   \
    B(2)  C(3)  
  /   \      \
 D(4)  E(5)   F(7)  

For first case(0—n-1),
if (say)father=p;
then left_son=(2*p)+1;
and right_son=(2*p)+2;

For second case(1—n),
if (say)father=p;
then left_son=(2*p);
and right_son=(2*p)+1;
'''

'''
Use cases:
heap: tree like data structure implemented in array to be used as a priority queue
B-,B+ tree: used to implement indexes in databases
syntax tree: used in compilers
K-D tree: A space partitioning tree used to organize points in K dimensional space.
Trie: implement dictionay for prefix lookup
suffix tree: pattern searching in a fied tex.
'''


# define node the building block of trees


class Node():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# insertion


def insert():
    pass
# deletion


def delete():
    pass

####################################################################################################
# let's find a better way to traverse the tree.

# traversal:
# (b) Preorder (Root, Left, Right) :  1 2 4 5 3
# (a) Inorder (Left, Root, Right) :   4 2 5 1 3
# (c) Postorder (Left, Right, Root) : 4 5 2 3 1


def inOrderTraversal(node,ary):

    if node is not None:
        inOrderTraversal(node.left,ary)
        ary.append(node.value)
        # print(str(node.value))
        inOrderTraversal(node.right,ary)

    return ary

def preOrderTraversal(node,ary):
    if node is not None:
        ary.append(node.value)
        preOrderTraversal(node.left,ary)
        preOrderTraversal(node.right,ary)
    
    return ary

def postOrderTraversal(node,ary):
    if node is not None:
        postOrderTraversal(node.left,ary)
        postOrderTraversal(node.right,ary)
        ary.append(node.value)

    return ary

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.right = Node(3)
    root.left.right = Node(5)

    print(type(root))
    print(isinstance(root, Node))

    og = []
    og.append(root.value)
    og.append(root.left.value)
    og.append(root.right.value)
    og.append(root.left.left.value)
    og.append(root.left.right.value)
    print("og: "+str(og))


    pre_order_ary = preOrderTraversal(root,[])
    print("pr: "+str(pre_order_ary))
    in_order_ary = inOrderTraversal(root,[])
    print("in: "+str(in_order_ary))
    post_order_ary=postOrderTraversal(root,[])
    print("po: "+str(post_order_ary))

    

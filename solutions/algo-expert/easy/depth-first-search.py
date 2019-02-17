'''
dfs: 
Time:O(V+E)
space = O(V), worst case we make a call stack for every vertex.

'''
# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # dfs means traverse as deep as you can before going back to your parent.
		
        # recursive call on the child
		array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        return array
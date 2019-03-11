# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
'''
bfs is to go as wide before doing deep.
we need to visit all nodes children,
then visit each children's child befor going deeper.
we need to keep track of the node's child
'''

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
		
		toVisit=[self]
		while len(toVisit) > 0:
			curr = toVisit.pop(0)
			array.append(curr.name)
			for child in curr.children:
				toVisit.append(child)
				
		return array
			
        

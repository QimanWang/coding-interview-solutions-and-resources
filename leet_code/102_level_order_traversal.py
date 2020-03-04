# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        
        q = [3]
        
        while q has more:
            q.pop()  #a level
            add l:9, r:20 to queue
            level size = len(q) = 2
            
            for i in range(level_size):
                pop 9, add it's child
                pop 20 add it's child 
        """
        if not root:
            return []

        q=[]
        q.append(root)
        res = []
        while len(q) > 0:
            level_nodes = []
            for i in range(len(q)):
                curr_node = q.pop(0)
                level_nodes.append(curr_node.val)
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
            res.append(level_nodes)
        return res
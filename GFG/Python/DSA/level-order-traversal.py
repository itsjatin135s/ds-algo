# https://www.geeksforgeeks.org/problems/level-order-traversal/1

class Solution:
    #Function to return the level order traversal of a tree.
    def level_order(self,root):
        # Code here
        res = []
        queue = [root]
        
        while len(queue):
            node = queue.pop(0)
            res.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
# https://www.geeksforgeeks.org/problems/minimum-depth-of-a-binary-tree/1

class Solution:
    def min_depth(self, root):
        #Code here
        if root == None:
            return 0
            
        depth = 0
        queue = [root]
        
        while len(queue):
            depth += 1
            loop_length = len(queue)
            for _ in range(0, loop_length):
                node = queue.pop(0)
                if node.left == None and node.right == None:
                    return depth
                    
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)
        return depth
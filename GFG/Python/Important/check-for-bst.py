# https://www.geeksforgeeks.org/problems/check-for-bst/1

class Solution:
    
    #Function to check whether a Binary Tree is BST or not.
    def is_bst(self, root):
        #code here
        if not root:
            return False
        
        def is_bst_util(node, left, right):
            if node == None:
                return True
            if not (left < node.data < right):
                return False
            return is_bst_util(node.left, left, node.data) and is_bst_util(node.right, node.data, right)
        
        return is_bst_util(root, float('-inf'), float('inf'))

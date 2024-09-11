# https://www.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1

class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def find_mid(self, head):
        # Code here
        # return the value stored in the middle node
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data
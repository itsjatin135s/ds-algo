# https://www.geeksforgeeks.org/problems/reverse-a-linked-list/1

class Solution:
    # Function to reverse a linked list.
    def reverse_list(self, head):
        # Code here
        node = head.next
        prev = head
        prev.next = None
        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp
        return prev

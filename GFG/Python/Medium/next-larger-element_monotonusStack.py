# https://www.geeksforgeeks.org/problems/next-larger-element-1587115620/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card
class Solution:
    def nextLargerElement(arr, n):
        # code here
        stack = []
        res = []
        for i in range(0, n):
            while stack and arr[n-i-1] >= stack[-1]:
                stack.pop()
            res.append(stack[-1]) if stack else res.append(-1)
            stack.append(arr[n-i-1])
        return res[::-1]

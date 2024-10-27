# https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1


class Solution:
    # #Complete this function
    # Function to find the sum of contiguous subarray with maximum sum.
    def max_sub_array_sum(self, arr):
        # #Your code here
        max_sum = float('-inf')
        curr_sum = 0

        for i in arr:
            if curr_sum < 0:
                curr_sum = 0

            curr_sum += i

            if curr_sum > max_sum:
                max_sum = curr_sum
        return max_sum

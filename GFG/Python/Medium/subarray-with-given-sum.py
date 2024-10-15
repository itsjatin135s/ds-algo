class Solution:
    def sub_array_sum(self, arr, s):
        curr_sum, prev_sums = 0, {}

        for i in range(len(arr)):
            curr_sum += arr[i]
            if curr_sum == s:
                return [1, i+1]
            if curr_sum - s in prev_sums:
                return [prev_sums[curr_sum-s] + 2, i+1]
            prev_sums[curr_sum] = i

        return [-1]

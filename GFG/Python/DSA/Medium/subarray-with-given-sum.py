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


#  my sol
def sub_array_sum_2(self, arr, s):
    # code here
    curr_sum = 0
    res = [0, 0]
    while res[1] < len(arr):
        if curr_sum > s:
            curr_sum -= arr[res[0]]
            res[0] += 1
        elif curr_sum < s:
            curr_sum += arr[res[1]]
            res[1] += 1
        if curr_sum == s:
            return [res[0]+1, res[1]]
        return [-1]

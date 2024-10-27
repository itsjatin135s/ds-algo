# https://www.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/1

class Solution:
    def longest_common_prefix(self, arr):
        # code here
        common_string = arr[0]
        
        for i in range(0, len(arr) - 1):
            temp_string = ''
            for j in range(0, min(len(arr[i]), len(arr[i + 1]))):
                if arr[i][j] != arr[i + 1][j]:
                    common_string = min(common_string, temp_string)
                else:
                    temp_string += arr[i][j]
                
        return common_string if len(common_string) > 0 else -1
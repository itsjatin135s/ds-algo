# https://www.geeksforgeeks.org/problems/smallest-subarray-with-sum-greater-than-x5651/1

def smallest_sub_with_sum(self, x, arr):
        # Your code goes here 
        start = 0
        end = 0
        min_length = len(arr) + 1
        curr_sum = 0
        
        for i in arr:
            curr_sum += i
            while curr_sum > x:
                min_length = min(min_length, end-start+1)
                curr_sum -= arr[start]
                start += 1
            end += 1
            
        return 0 if min_length == len(arr) + 1 else min_length
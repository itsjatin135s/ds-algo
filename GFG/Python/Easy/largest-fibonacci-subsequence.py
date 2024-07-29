# https://www.geeksforgeeks.org/problems/largest-fibonacci-subsequence2206/1


class Solution:
    def find_fib_subset(self, arr, n):
        # code here
        res = []
        for i in arr:
            # print(i)
            if self.is_fibonacci(i):
                res.append(i)
        return res
    
    def is_fibonacci(self, n):
        return self.is_perfect_square(5*n*n + 4) or self.is_perfect_square(5*n*n - 4)
        
    def is_perfect_square(self, num):
        s = int(num ** 0.5)
        return s*s == num
# https://www.geeksforgeeks.org/problems/is-binary-number-multiple-of-30654/1


# Manual version
class Solution:
    def is_divisible(self, s):
        # code here
        n = len(s)
        num = 0
        for i in range(0, n):
            if s[n-1-i] != '0':
                num += pow(2, i)
        return 1 if num % 3 == 0 else 0


# Inbuilt method
def is_divisible(self, s):
    # code here
    num = int(s, 2)
    # Check divisibility by 3
    return 1 if num % 3 == 0 else 0

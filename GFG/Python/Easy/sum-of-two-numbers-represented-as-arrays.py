# https://www.geeksforgeeks.org/problems/sum-of-two-numbers-represented-as-arrays3110/1


class Solution:
    def find_sum(self, arr1, arr2):
        # code here
        num1 = ""
        num2 = ""
        for i in arr1:
            num1 += str(i)

        for i in arr2:
            num2 += str(i)

        res = int(num1) + int(num2)

        return [x for x in str(res)]

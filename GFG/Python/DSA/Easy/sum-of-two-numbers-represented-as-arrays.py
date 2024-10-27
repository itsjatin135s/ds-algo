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


# DSA Type Approach
class Solution1:
    def find_sum(self, arr1, arr2):
        # code here
        carry = 0
        res = []
        arr1 = arr1[::-1]
        arr2 = arr2[::-1]

        n = min(len(arr1), len(arr2))

        for i in range(0, n):
            j = arr1[i] + arr2[i] + carry
            if j >= 10:
                res.append(j-10)
                carry = 1
                continue
            res.append(j)
            carry = 0

        arr = arr1[n:] if arr1[n:] else arr2[n:]

        for i in arr:
            j = i + carry
            if j >= 10:
                res.append(j-10)
                carry = 1
                continue
            res.append(j)
            carry = 0

        if carry:
            res.append(carry)

        return res[::-1]


# optimized approach
class Solution2:
    def find_sum(self, arr1, arr2):
        carry = 0
        res = []

        # Reverse both arrays to add from the least significant digit
        arr1 = arr1[::-1]
        arr2 = arr2[::-1]

        # Find the maximum length to handle both arrays simultaneously
        max_len = max(len(arr1), len(arr2))

        for i in range(max_len):
            digit1 = arr1[i] if i < len(arr1) else 0
            digit2 = arr2[i] if i < len(arr2) else 0

            total = digit1 + digit2 + carry
            res.append(total % 10)
            carry = total // 10

        # If there's a carry left at the end, append it
        if carry:
            res.append(carry)

        # Reverse the result to get the final sum in correct order
        return res[::-1]

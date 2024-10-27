# https://www.geeksforgeeks.org/problems/find-equal-point-in-string-of-brackets2542/1

class Solution:
    def find_index(self, string):
        n = len(string)

        closing_brackets = 0
        for i in string:
            if i == ')':
                closing_brackets += 1

        opening_bracket = 0
        for i in range(0, n):
            if string[i] == '(':
                opening_bracket += 1
            else:
                closing_brackets -= 1

            if opening_bracket == closing_brackets:
                return i + 1
        return 0

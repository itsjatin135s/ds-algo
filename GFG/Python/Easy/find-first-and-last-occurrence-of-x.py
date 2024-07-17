#  https://www.geeksforgeeks.org/problems/find-first-and-last-occurrence-of-x0849/1


# My Solution 

class Solution:
    def indexes(self, v, x):
        # Your code goes here
        left_index = 0
        right_index = len(v) - 1
        res = [-1,-1]
        
        while left_index <= right_index:
            middle_index = (left_index + right_index)//2
            
            if v[middle_index] == x:
                res = [middle_index, middle_index]
                break
            if v[middle_index] > x:
                right_index = middle_index - 1
            else:
                left_index = middle_index + 1
        if res[0] > -1:
            while (middle_index - 1) > -1 and v[res[0]] == v[middle_index - 1]:
                middle_index -= 1
                res[0] = middle_index
                res[1] = middle_index
            while (middle_index + 1) < len(v) and v[res[1]] == v[middle_index+1]:
                middle_index += 1
                res[1] = middle_index
        return res

'''
SHORTCOMINGS AND IMPROVEMENTS:

1. Separation of Concerns:

    Original Code: The original implementation attempts to find both the first and last occurrences within a single loop. This complicates the logic, making it harder to maintain and understand.
    Optimized Code: The optimized version separates the search for the first and last occurrences into two distinct binary search functions. This separation makes the code cleaner, easier to understand, and maintain.

2. Efficiency:

    Original Code: After finding an occurrence, the original code continues to linearly scan to the left and right to find the boundaries. This can degrade performance to O(n)O(n) in the worst case if many elements match the target.
    Optimized Code: By using two distinct binary searches, each with O(log⁡n)O(logn) complexity, the optimized code ensures that the overall complexity remains O(log⁡n)O(logn), which is more efficient for large arrays.

3. Readability and Maintainability:

    Original Code: The nested while loops and conditional checks within the single binary search make the logic more complex and harder to follow.
    Optimized Code: The clear distinction between the two phases of finding the first and last occurrences makes the code more readable and easier to debug or modify.

'''

# OPTIMIZED CODE    

def indexes(self, v, x):
    def find_first(v, x):
        left_index, right_index = 0, len(v) - 1
        first = -1
        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2
            if v[middle_index] == x:
                first = middle_index
                right_index = middle_index - 1  # Continue searching in the left half
            elif v[middle_index] > x:
                right_index = middle_index - 1
            else:
                left_index = middle_index + 1
        return first

    def find_last(v, x):
        left_index, right_index = 0, len(v) - 1
        last = -1
        while left_index <= right_index:
            middle_index = (left_index + right_index) // 2
            if v[middle_index] == x:
                last = middle_index
                left_index = middle_index + 1  # Continue searching in the right half
            elif v[middle_index] > x:
                right_index = middle_index - 1
            else:
                left_index = middle_index + 1
        return last

    first_index = find_first(v, x)
    last_index = find_last(v, x)
    return [first_index, last_index]

# Example usage:
v = [1, 2, 2, 2, 3, 4, 5]
x = 2
solution = Solution()
print(solution.indexes(v, x))  # Output: [1, 3]

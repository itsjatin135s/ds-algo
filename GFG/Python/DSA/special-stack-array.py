# https://www.geeksforgeeks.org/problems/special-stack/1

# function should append an element on to the stack
def push(arr, ele):
    # Code here
    arr.append(ele)

# Function should pop an element from stack
def pop(arr):
    # Code here
    arr.pop(0)
# function should return 1/0 or True/False
def is_full(n, arr):
    # Code here
    return len(arr) == n
# function should return 1/0 or True/False
def is_empty(arr):
    #Code here
    return len(arr) == 0
# function should return minimum element from the stack
def get_min(n, arr):
    # Code here
    if isEmpty(arr):
        return False
        
    min_num = arr[0]
    for i in arr:
        min_num = min(min_num, i)
    return min_num
def binary_search(arr, target):
    if len(arr) < 1:
        return False
    left_index = 0
    right_index = len(arr) - 1
    while left_index <= right_index:
        middle_index = left_index + (right_index - left_index)//2
        if arr[middle_index] == target:
            return middle_index
        if arr[middle_index] > target:
            right_index = middle_index - 1
        if arr[middle_index] < target:
            left_index = middle_index + 1
    return False


print(binary_search([1, 2, 34], 4))

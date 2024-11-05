def move_zeros_to_end(arr):
    if len(arr) < 1:
        return arr

    n = len(arr) - 1
    zero_index = 0
    num_index = 0

    while num_index <= n:
        if arr[num_index] != 0:
            arr[zero_index], arr[num_index] = arr[num_index], arr[zero_index]
            zero_index += 1
        num_index += 1
    return arr


test1 = [1, 2, 3, 0, 4]
test2 = [0, 0, 4]
test3 = [0, 0]
test4 = [0, 1, 2, 43, 3]

print(move_zeros_to_end(test4))

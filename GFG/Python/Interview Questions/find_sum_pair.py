def find_sum_pair(arr, target):
    num_index = {}

    for i in range(0, len(arr)):
        compliment = target - arr[i]
        if compliment in num_index.keys():
            return [num_index[compliment], i]
        else:
            num_index[arr[i]] = i
    return False


print(find_sum_pair([3, 2, 4], 6))

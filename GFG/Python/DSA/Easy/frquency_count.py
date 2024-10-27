def frequencyCount(arr, N, P):
    #  do modify in the given array
    res = [0]*P

    for i in arr:
        res[i-1] += 1

    return res

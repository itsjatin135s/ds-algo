def bubble_sort(arr):
    swap = True

    while swap:
        swap = False
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap = True
    return arr


print(bubble_sort([1, 3, 2, 6, 4]))

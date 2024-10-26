class Solution:
    def quickSort(self, arr, low, high):
        # code here
        if low < high:
            partition_index = self.partition(arr, low, high)
            self.quickSort(arr, low, partition_index-1)
            self.quickSort(arr, partition_index+1, high)
        return arr

    def partition(self, arr, low, high):
        # code here
        pivot = arr[low]
        i = low
        j = high

        while i < j:
            # print('inner', i, j, arr)
            while arr[i] <= pivot and i < high:
                i += 1

            while arr[j] > pivot and j > low:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        (i, j, arr)
        arr[low], arr[j] = arr[j], arr[low]
        return j


method = Solution()

print(method.quickSort([4, 1, 3, 9, 7], 0, 4))

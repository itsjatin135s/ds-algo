class Solution:
    # Function to return the position of the first repeating element.
    def first_repeated(self, arr):

        # arr : given array
        # n : size of the array
        mapper = {}
        n = len(arr)
        res = n

        for i in range(0, n):
            if arr[i] in mapper:
                if res > mapper[arr[i]]:
                    res = mapper[arr[i]]
            else:
                mapper[arr[i]] = i
        return -1 if res == n else res+1

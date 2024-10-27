# https://www.geeksforgeeks.org/problems/search-in-a-matrix17201720/1

class Solution:
    def mat_search(self, mat, n, m, x):
        # Complete this function
        height = 0
        width = m-1

        while height <= n-1 and width >= 0:
            if mat[height][width] == x:
                return 1
            if mat[height][width] > x:
                width -= 1
            else:
                height += 1

        return 0

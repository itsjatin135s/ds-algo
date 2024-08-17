class Solution:
    def mat_search(self, mat, N, M, X):
        # Complete this function
        height = 0
        width = M-1

        while height <= N-1 and width >= 0:
            if mat[height][width] == X:
                return 1
            if mat[height][width] > X:
                width -= 1
            else:
                height += 1

        return 0

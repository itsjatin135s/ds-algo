# https://www.geeksforgeeks.org/problems/addition-of-submatrix5835/1

class Solution:

	def sub_matrix_sum(self,arr, n, m, x1, y1, x2, y2):
		# code here
		if x1 > x2 or y1 > y2:
		    return 0
		    
    result = 0
        
        for i in range(x1-1,x2):
            for j in range(y1-1,y2):
                result += arr[i][j]
        
        return result
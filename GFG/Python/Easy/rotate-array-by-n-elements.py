# https://www.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1


# waste of time solution just written for GFG to accept it

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotate_arr(self,arr,d,n):
        #Your code here
        d %= n
        if d == 0:
            return
        
        def reverse(i, j):
            while i < j:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        
        reverse(0, d - 1)
        reverse(d, n - 1)
        reverse(0, n - 1)

# Much much efficient sol

def rotate_arr(a,d,n):
    # Ensure D is within the bounds of N
    d = d % n
    # Rotate the array by slicing
    return a[d:] + a[:d]

# Even Better

def rotate_arr(a,d,n):
    #Your code here
    return a[d:]+a[:n]

print(rotateArr([1,2,3,4,5], 2, 5))

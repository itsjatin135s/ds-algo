# https://www.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1
def remove_duplicate(self, arr):
    #Code Here
    unique_index = 1    
    for i in range(1, len(arr)):
        if(arr[i] != arr[i-1]):
            arr[unique_index] = arr[i]
            unique_index += 1
    
    # print('here', unique_index)   
    return unique_index
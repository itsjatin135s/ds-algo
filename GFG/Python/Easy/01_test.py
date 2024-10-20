def get_x_sum(subarray, x):
    # Step 1: Manually count the occurrences of elements
    freq = {}
    for num in subarray:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    
    # Step 2: Sort elements by frequency (descending), and by value (descending) in case of ties
    sorted_elements = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
    print(sorted_elements)
    
    # Step 3: Select the top x most frequent elements and calculate the x-sum
    x_sum = 0
    for i in range(min(x, len(sorted_elements))):  # Handle case when there are less than x elements
        value, count = sorted_elements[i]
        x_sum += value * count
    
    return x_sum

def x_sum_of_subarrays(nums, k, x):
    n = len(nums)
    answer = []
    
    # Step 4: Slide over the array to get each subarray of length k
    for i in range(n - k + 1):
        subarray = nums[i:i + k]
        answer.append(get_x_sum(subarray, x))
    
    return answer

# Example usage:
nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
k = 3
x = 2
result = x_sum_of_subarrays(nums, k, x)
print(result)

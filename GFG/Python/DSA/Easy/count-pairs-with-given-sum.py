# https://www.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1


class Solution:
    def get_pairs_count(self, arr, num):
        # code here
        # Dictionary to store the frequency of each element
        freq = {}
        result = 0

        # Loop through each element in the array
        for i in arr:
            # Check if the complementary value (num - i) is already in the frequency dictionary
            if (num - i) in freq:
                # If found, add the frequency of the complementary value to the result
                result += freq[num - i]

            # Update the frequency of the current element in the dictionary
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        # Return the total count of pairs
        return result
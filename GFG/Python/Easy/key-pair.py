# https://www.geeksforgeeks.org/problems/key-pair5616/1


class Solution:
    def has_array_two_candidates(self, arr, x):
        # Initialize an empty set to store elements
        storage = set()

        # Loop through each element in the array
        for i in arr:
            # Check if the complementary value (x - i) is already in the set
            if (x - i) in storage:
                # If found, return True
                return True
            # Add the current element to the set if not already present
            storage.add(i)

        # If no pairs are found, return False
        return False

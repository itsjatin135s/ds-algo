class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        
        start = 0
        freq = {}
        res = []

        while start+k <= len(nums):
            temp_arr = nums[start: start+k]
            for i in temp_arr:
                if i in freq:
                    freq[i] += 1
                else:
                    freq[i] = 1
            x_sum = 0
            sorted_elements = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
            for i in range(min(x, len(sorted_elements))):
                value, count = sorted_elements[i]
                x_sum += value * count
            res.append(x_sum)
            freq = {}
            start += 1
        
        return res
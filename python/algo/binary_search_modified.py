# https://leetcode.com/problems/search-insert-position/submissions/1424765908/


class Solution:
    def search_insert(self, nums, target: int) -> int:
        if len(nums) < 1:
            return 0
        right = 0
        left = len(nums) - 1
        mid = 0
        while right <= left:
            mid = (right+(left-right)//2)
            num = nums[mid]
            if num > target:
                left = mid - 1
            elif num < target:
                right = mid + 1
            else:
                return mid
        return right

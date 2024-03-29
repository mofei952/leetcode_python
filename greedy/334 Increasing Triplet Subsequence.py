"""
question:
https://leetcode.com/problems/increasing-triplet-subsequence/
"""
from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        has_little_indexes = set()
        min_val = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > min_val:
                has_little_indexes.add(i)
            else:
                min_val = nums[i]
        max_value = nums[len(nums) - 1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < max_value:
                if i in has_little_indexes:
                    return True
            else:
                max_value = nums[i]
        return False

    def increasingTriplet2(self, nums: List[int]) -> bool:
        """
            Time: O(n)
            Space: O(1)
        """
        first = float('inf')
        second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
        return False


if __name__ == '__main__':
    assert Solution().increasingTriplet2([1, 2, 3, 4, 5]) is True
    assert Solution().increasingTriplet2([5, 4, 3, 2, 1]) is False
    assert Solution().increasingTriplet2([2, 1, 5, 0, 4, 6]) is True
    assert Solution().increasingTriplet2([2]) is False
    assert Solution().increasingTriplet2([1, 2]) is False

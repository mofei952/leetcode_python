"""
question:
https://leetcode.com/problems/jump-game-ii/
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        start = end = count = 0
        while end < len(nums) - 1:
            count += 1
            max_distance = end + 1
            for i in range(start, end + 1):
                max_distance = max(max_distance, i + nums[i])
            start, end = end + 1, max_distance
        return count

    def jump2(self, nums: List[int]) -> int:
        near = far = count = 0
        for i in range(len(nums)):
            if i > near:
                near = far
                count += 1
            far = max(far, i + nums[i])
        return count


if __name__ == '__main__':
    assert Solution().jump([2, 3, 1, 1, 4]) == 2

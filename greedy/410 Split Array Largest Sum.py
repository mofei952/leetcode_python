"""
question:
https://leetcode.com/problems/split-array-largest-sum/
"""
from typing import List


class Solution:
    def vaild(self, nums, target, m):
        total, count = 0, 1
        for n in nums:
            total += n
            if total > target:
                total = n
                count += 1
                if count > m:
                    return False
        return True

    def splitArray(self, nums: List[int], m: int) -> int:
        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l + r) // 2
            if self.vaild(nums, mid, m):
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == '__main__':
    assert Solution().splitArray([7, 2, 5, 10, 8], 2) == 18
    assert Solution().splitArray([1, 2, 3, 4, 5], 2) == 9
    assert Solution().splitArray([1, 4, 4], 3) == 4

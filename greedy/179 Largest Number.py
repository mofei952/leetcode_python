"""
question:
https://leetcode.com/problems/largest-number/
"""
import functools
from typing import List


class Solution:
    def compare(self, x, y):
        return x + y < y + x

    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        for i in range(1, len(nums)):
            temp = nums[i]
            j = i - 1
            while j >= 0 and self.compare(nums[j], temp):
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = temp
        return str(int(''.join(nums)))

    def compare2(self, x, y):
        if x + y < y + x:
            return 1
        return -1

    def largestNumber2(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]
        nums.sort(key=functools.cmp_to_key(self.compare2))
        return str(int(''.join(nums)))


if __name__ == '__main__':
    assert Solution().largestNumber2([10, 2]) == '210'
    assert Solution().largestNumber2([3, 30, 34, 5, 9]) == '9534330'
    assert Solution().largestNumber2([0, 0]) == '0'

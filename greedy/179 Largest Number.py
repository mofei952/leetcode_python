"""
question:
https://leetcode.com/problems/largest-number/
"""
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(1, len(nums)):
            temp = nums[i]
            j = i - 1
            while j >= 0 and self.compare(nums[j], nums[i]):
                j -= 1
            for k in range(i, j + 1, -1):
                nums[k] = nums[k - 1]
            nums[j + 1] = temp
        return str(int(''.join(map(str, nums))))

    def compare(self, x, y):
        return str(x) + str(y) < str(y) + str(x)


if __name__ == '__main__':
    assert Solution().largestNumber([10, 2]) == '210'
    assert Solution().largestNumber([3, 30, 34, 5, 9]) == '9534330'
    assert Solution().largestNumber([0, 0]) == '0'

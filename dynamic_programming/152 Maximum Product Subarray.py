"""
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""

from typing import List
from itertools import accumulate
from functools import reduce


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_num = min_num = 1
        max_product = float('-inf')
        for num in nums:
            num1 = max_num * num
            num2 = min_num * num
            max_num = max(num, num1, num2)
            min_num = min(num, num1, num2)
            max_product = max(max_product, max_num)
        return max_product

    def maxProduct2(self, nums: List[int]) -> int:
        max1 = max(accumulate(nums, lambda a, b: (a * b) or b))
        max2 = max(accumulate(reversed(nums), lambda a, b: (a * b) or b))
        return max(max1, max2)


if __name__ == "__main__":
    print(Solution().maxProduct2([2, 3, -2, 4]))
    print(Solution().maxProduct2([-2, 0, -1]))
    print(Solution().maxProduct2([-2, 3, -4]))

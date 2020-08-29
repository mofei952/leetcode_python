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


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        min_num = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]*nums[i], min_num*nums[i])
            min_num = min(nums[i], dp[i-1]*nums[i], min_num*nums[i])
        return max(dp)


if __name__ == "__main__":
    print(Solution().maxProduct([2, 3, -2, 4]))
    print(Solution().maxProduct([-2, 0, -1]))
    print(Solution().maxProduct([-2, 3, -4]))

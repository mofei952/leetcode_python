"""
You are a professional robber planning to rob houses along a street. 
Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, 
and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, 
return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [0]
Output: 0
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        return max(self._rob(nums, 0, len(nums)-1), self._rob(nums, 1, len(nums)))
    
    def _rob(self, nums: List[int], low, high):
        if high - low <= 2:
            return max(nums[low: high])

        dp = [0] * (high-low)
        dp[0] = nums[low]
        dp[1] = max(nums[low], nums[low+1])

        for i in range(2, high-low):
            index = i+low
            dp[i] = max(dp[i-1], dp[i-2]+nums[index])

        return dp[-1]


if __name__ == "__main__":
    print(Solution().rob([2, 3, 2]))
    print(Solution().rob([1, 2, 3, 1]))
    print(Solution().rob([0]))
    print(Solution().rob([0, 0]))

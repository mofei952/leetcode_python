"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_left = max_right = 0
        capacity = 0
        while left < right:
            if height[left] <= height[right]:
                if height[left] >= max_left:
                    max_left = height[left]
                else:
                    capacity += max_left - height[left]
                left += 1
            else:
                if  height[right] >= max_right:
                    max_right = height[right]
                else:
                    capacity += max_right - height[right]
                right -= 1
        return capacity

if __name__ == "__main__":
    print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))
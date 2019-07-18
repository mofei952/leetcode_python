#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/16 19:07
# @File    : 011 Container With Most Water.py
# @Software: PyCharm

"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example:
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        low, high = 0, len(height) - 1
        max_area = 0
        while low < high:
            if height[low] < height[high]:
                area = height[low] * (high- low)
                low += 1
            else:
                area = height[high] * (high - low)
                high -= 1
            max_area = max(max_area, area)
        return max_area


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))

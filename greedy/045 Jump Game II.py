#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/25 20:58
# @File    : 045 Jump Game II.py
# @Software: PyCharm

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

Example:
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

Note:
You can assume that you can always reach the last index.
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
    print(Solution().jump2([2, 3, 1, 1, 4]))

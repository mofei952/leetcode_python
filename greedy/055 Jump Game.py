#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/25 20:45
# @File    : 055 Jump Game.py
# @Software: PyCharm

"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:
Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_distance = 0
        for i in range(len(nums)):
            if i > max_distance:
                return False
            max_distance = max(max_distance, i + nums[i])
        return True


if __name__ == '__main__':
    print(Solution().canJump([2, 3, 1, 1, 4]))
    print(Solution().canJump([3, 2, 1, 0, 4]))
    print(Solution().canJump([2, 0, 0]))

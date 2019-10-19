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

from commons import running_time


class Solution:
    @running_time
    def canJump(self, nums: List[int]) -> bool:
        max_distance = 0
        for i in range(len(nums)):
            if i > max_distance:
                return False
            max_distance = max(max_distance, i + nums[i])
        return True

    @running_time
    def canJump2(self, nums: List[int]) -> bool:
        last_index = len(nums) - 1
        for i in range(last_index - 1, -1, -1):
            if i + nums[i] >= last_index:
                last_index = i
        return last_index == 0


if __name__ == '__main__':
    assert Solution().canJump([2, 3, 1, 1, 4]) is True
    assert Solution().canJump2([2, 3, 1, 1, 4]) is True

    assert Solution().canJump([3, 2, 1, 0, 4]) is False
    assert Solution().canJump2([3, 2, 1, 0, 4]) is False

    assert Solution().canJump([2, 0, 0]) is True
    assert Solution().canJump2([2, 0, 0]) is True

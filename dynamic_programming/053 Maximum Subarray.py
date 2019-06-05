#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/11/7 19:00
# @File    : 053 Maximum Subarray.py
# @Software: PyCharm

"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

from typing import List

from commons import running_time


class Solution:
    @running_time
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) <= 0:
            return max(nums)
        max_value = value = 0
        for n in nums:
            value = max(value, 0)
            value += n
            max_value = max(max_value, value)
        return max_value

    @running_time
    def maxSubArray2(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)


if __name__ == '__main__':
    list_ = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert Solution().maxSubArray(list_) == 6
    assert Solution().maxSubArray2(list_) == 6

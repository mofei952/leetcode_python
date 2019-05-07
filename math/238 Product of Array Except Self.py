#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/7 19:45
# @File    : 238 Product of Array Except Self.py
# @Software: PyCharm

"""
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the purpose of space complexity analysis.)
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        s = 1
        zero_count = 0
        for n in nums:
            if n == 0:
                zero_count += 1
                continue
            s *= n
        if zero_count > 1:
            return [0] * len(nums)
        res = []
        for n in nums:
            if zero_count:
                res.append(0 if n else s)
            else:
                res.append(s // n)
        return res


if __name__ == '__main__':
    print(Solution().productExceptSelf([0, 0, 1]))

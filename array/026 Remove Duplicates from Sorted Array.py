#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/29 20:45
# @File    : 026 Remove Duplicates from Sorted Array.py
# @Software: PyCharm

"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,2,2,3,3,4],
Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
It doesn't matter what values are set beyond the returned length.
"""
import random
from copy import copy
from typing import List

from commons import running_time


class Solution:
    @running_time
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)

    @running_time
    def removeDuplicates2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1


if __name__ == '__main__':
    v = 1
    data = []
    for j in range(100000):
        data.append(v)
        v += random.randint(0, 1)

    data1 = copy(data)
    len1 = Solution().removeDuplicates(data1)

    data2 = copy(data)
    len2 = Solution().removeDuplicates2(data2)

    assert data1[:len1] == data2[:len2]

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/11 20:39
# @File    : 080 Remove Duplicates from Sorted Array II.py
# @Software: PyCharm

"""
Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:
Given nums = [1,1,1,2,2,3],
Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It doesn't matter what you leave beyond the returned length.

Example 2:
Given nums = [0,0,1,1,1,1,2,3,3],
Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.
It doesn't matter what values are set beyond the returned length.
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        i = 2
        for j in range(2, len(nums)):
            if nums[j] > nums[i - 2]:
                nums[i] = nums[j]
                i += 1
        return i


if __name__ == '__main__':
    print(Solution().removeDuplicates([1]))
    print(Solution().removeDuplicates([1, 1, 1, 2, 2, 3]))
    print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))

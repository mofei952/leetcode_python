#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/3/20 17:56
# @File    : 153 Find Minimum in Rotated Sorted Array.py
# @Software: PyCharm

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
You may assume no duplicate exists in the array.

Example 1:
Input: [3,4,5,1,2]
Output: 1

Example 2:
Input: [4,5,6,7,0,1,2]
Output: 0
"""
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """在升序排列并移动未知位置的列表中查询最小值"""
        if not nums:
            return -1
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if mid == low:
                return min(nums[low], nums[high])
            if nums[mid] == nums[high]:
                if nums[low] < nums[mid]:
                    return nums[low]
                else:
                    return nums[high]
            elif nums[mid] < nums[high]:
                if nums[low] < nums[mid]:
                    return nums[low]
                else:
                    high = mid
            else:
                low = mid
        return nums[low]

    def findMin2(self, nums: List[int]) -> int:
        """在升序排列并移动未知位置的列表中查询最小值 优化后"""
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if mid >= 1 and nums[mid - 1] > nums[mid]:
                return nums[mid]
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]


def test_153():
    assert Solution().findMin2([2, 1]) == 1
    assert Solution().findMin2([1, 2]) == 1
    assert Solution().findMin2([3, 1, 2]) == 1
    assert Solution().findMin2([3, 4, 5, 1, 2]) == 1
    assert Solution().findMin2([4, 5, 6, 7, 0, 1, 2]) == 0

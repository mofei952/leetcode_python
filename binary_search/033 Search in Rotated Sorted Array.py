#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/11/6 12:53
# @File    : 033 Search in Rotated Sorted Array.py
# @Software: PyCharm

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """在升序排列并移动未知位置的列表中 查找target的位置"""
        if not nums:
            return -1
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                if target >= nums[low] or nums[low] > nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target <= nums[high] or nums[high] < nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1


if __name__ == '__main__':
    list = [4, 5, 6, 7, 0, 1, 2]
    test_list = [4, 5, 6, 7, 0, 1, 2, 8, 3]
    for i in test_list:
        result = Solution().search(list, i)
        print(result)

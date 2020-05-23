#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/5/23 17:45
# @File    : 081 Search in Rotated Sorted Array II.py
# @Software: PyCharm

"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).
You are given a target value to search. If found in the array return true, otherwise return false.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Follow up:
This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return True
            while low < mid and nums[low] == nums[mid]:
                low += 1
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False


if __name__ == '__main__':
    nums = [2, 5, 6, 0, 0, 1, 2]
    test_nums = range(-1, 8)
    for i in test_nums:
        print(i, Solution().search(nums, i))
    print()

    print(Solution().search([1, 1, 3, 1], 3))
    print()
    print(Solution().search([1, 3, 1, 1, 1], 3))
    print()
    print(Solution().search([3, 1], 1))
    print()
    print(Solution().search([3, 1, 1], 3))

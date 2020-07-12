#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/15 19:47
# @File    : 078 Subsets.py
# @Software: PyCharm

"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(index, temp_list):
            if index == len(nums):
                result.append(list(temp_list))
                return
            dfs(index + 1, temp_list)
            dfs(index + 1, temp_list + [nums[index]])

        result = []
        dfs(0, [])
        return result

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            result.extend([subset + [num] for subset in result])
        return result


if __name__ == '__main__':
    print(Solution().subsets2([1, 2, 3]))

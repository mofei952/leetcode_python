#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/7 19:26
# @File    : 047 Permutations II.py
# @Software: PyCharm

"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, temp):
            if not nums:
                res.append(list(temp))
                return
            for i, v in enumerate(nums):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                nums.pop(i)
                temp.append(v)
                dfs(nums, temp)
                temp.pop()
                nums.insert(i, v)
        nums.sort()
        res = []
        dfs(nums, [])
        return res


if __name__ == '__main__':
    print(Solution().permuteUnique([3,3,0,3]))

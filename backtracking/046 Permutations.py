#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/9 18:21
# @File    : 046 Permutations.py
# @Software: PyCharm

"""
Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, temp):
            if not nums:
                res.append(list(temp))
                return
            for i, n in enumerate(nums):
                nums.pop(i)
                temp.append(n)
                dfs(nums, temp)
                temp.pop()
                nums.insert(i, n)
        res = []
        dfs(nums, [])
        return res


if __name__ == '__main__':
    result = Solution().permute([1, 2, 3])
    print(result)

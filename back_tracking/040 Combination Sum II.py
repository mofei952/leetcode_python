#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/4 18:56
# @File    : 040 Combination Sum II.py
# @Software: PyCharm

"""
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = set()
        def dfs(start, nums, target):
            if target == 0:
                result.add(tuple(nums))
                return
            if start == len(candidates):
                return
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                if candidate > target:
                    break
                if i != start and candidate == candidates[i-1]:
                    continue
                nums.append(candidate)
                dfs(i + 1, nums, target - candidate)
                nums.pop()
        dfs(0, [], target)
        return list(result)


if __name__ == '__main__':
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(Solution().combinationSum2([2, 5, 2, 1, 2], 5))

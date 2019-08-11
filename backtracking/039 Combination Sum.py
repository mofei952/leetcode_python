#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/4 18:30
# @File    : 039 Combination Sum.py
# @Software: PyCharm

"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.
The same repeated number may be chosen from candidates unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:
Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def dfs(index, nums, target):
            if target == 0:
                result.append(list(nums))
                return
            for i in range(index, len(candidates)):
                candidate = candidates[i]
                if target < candidate:
                    break
                nums.append(candidate)
                dfs(i, nums, target - candidate)
                nums.pop()
        dfs(0, [], target)
        return result


if __name__ == '__main__':
    result = Solution().combinationSum([2, 3, 6, 7], 7)
    print(result)

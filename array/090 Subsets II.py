#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/15 20:13
# @File    : 090 Subsets II.py
# @Software: PyCharm

"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = {()}
        for num in nums:
            temp_set = set()
            for subset in result:
                temp = subset + (num,)
                if temp not in result:
                    temp_set.add(temp)
            result |= temp_set
        return list(result)


if __name__ == '__main__':
    res = Solution().subsetsWithDup([4, 4, 4, 1, 4])
    print(res)

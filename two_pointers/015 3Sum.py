#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/19 20:37
# @File    : 015 3Sum.py
# @Software: PyCharm

"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""

from collections import defaultdict
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        if n < 3:
            return []

        nums.sort()
        map = {v: i for i, v in enumerate(nums)}
        hi = nums[-1]

        result = []
        for i in range(n - 2):
            if i and nums[i] == nums[i - 1]: continue
            a = nums[i]
            if a + 2 * hi < 0: continue
            if 3 * a > 0: break
            for j in range(i + 1, n - 1):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                b = nums[j]
                if a + b + hi < 0: continue
                if a + 2 * b > 0: break
                c = 0 - a - b
                if c in map and map[c] > j:
                    result.append([a, b, c])

        return result

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        result = []
        if 0 in counts and counts[0] >= 3:
            result.append([0, 0, 0])

        nums = counts.keys()
        positive_nums, negative_nums = [], []
        for num in nums:
            if num >= 0:
                positive_nums.append(num)
            else:
                negative_nums.append(num)

        for pos in positive_nums:
            for neg in negative_nums:
                other = -(pos + neg)
                if other not in counts:
                    continue
                if (neg < other < pos
                        or other == pos and counts[other] > 1
                        or other == neg and counts[other] > 1):
                    result.append([pos, other, neg])

        return result


if __name__ == '__main__':
    print(Solution().threeSum2([1, -1]))
    print(Solution().threeSum2([0, 0, 0, 0]))
    print(Solution().threeSum2([-1, 0, 1, 2, -1, -4]))
    print(Solution().threeSum2([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))

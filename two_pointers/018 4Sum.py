#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/3/29 20:51
# @File    : 18 4Sum.py
# @Software: PyCharm


"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.

Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""
from collections import defaultdict
from typing import List

import pytest

from commons import func_test


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []

        nums.sort()

        res = []
        for i in range(n - 3):
            if i and nums[i] == nums[i - 1]: continue
            if sum(nums[i:i + 4]) > target: break
            if sum([nums[i], *nums[n - 3:]]) < target: continue
            for j in range(i + 1, n - 2):
                if j != i + 1 and nums[j] == nums[j - 1]: continue
                if nums[i] + sum(nums[j:j + 3]) > target: break
                if sum([nums[i], nums[j], *nums[n - 2:]]) < target: continue
                nums_list = self.twoSum(nums, j + 1, n - 1, target - nums[i] - nums[j])
                if nums_list:
                    a = [nums[i], nums[j]]
                    res.extend(a + nums_ for nums_ in nums_list)
        # print(res)
        return res

    def twoSum(self, nums, start, end, target):
        res = []
        low, high = start, end
        while low < high:
            s = nums[low] + nums[high]
            if s == target:
                pick = [nums[low], nums[high]]
                if pick not in res:
                    res.append(pick)
                low += 1
                high -= 1
            elif s < target:
                low += 1
            else:
                high -= 1
        return res

    def fourSum2(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []

        nums.sort()
        map = {v: i for i, v in enumerate(nums)}
        hi = nums[-1]

        res = []
        for i in range(n - 3):
            if i and nums[i] == nums[i - 1]: continue
            a = nums[i]
            if a + 3 * hi < target: continue
            if 4 * a > target: break
            for j in range(i + 1, n - 2):
                if j != i + 1 and nums[j] == nums[j - 1]: continue
                b = nums[j]
                if a + b + 2 * hi < target: continue
                if a + 3 * b > target: break
                for k in range(j + 1, n - 1):
                    if k != j + 1 and nums[k] == nums[k - 1]: continue
                    c = nums[k]
                    if a + b + c + hi < target: continue
                    if a + b + 2 * c > target: break
                    d = target - a - b - c
                    if d in map and map[d] > k:
                        res.append([a, b, c, d])
        # print(res)
        return res

    def fourSum3(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        nums.sort()
        min_ = nums[0] + nums[1]
        max_ = nums[-2] + nums[-1]
        left = max(min_, target - max_)
        right = min(max_, target - min_)
        map = defaultdict(list)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                value = nums[i] + nums[j]
                if value < left:
                    continue
                if value > right:
                    continue
                map[value].append([i, j])
        result = []
        for v in map:
            v2 = target - v
            if v2 not in map:
                continue
            for i in map[v]:
                for j in map[v2]:
                    if not i[0] < i[1] < j[0] < j[1]:
                        continue
                    array = [nums[i[0]], nums[i[1]], nums[j[0]], nums[j[1]]]
                    if array not in result:
                        result.append(array)
        return sorted(result)


# pytest -vv --durations=10 -q --tb=line "018 4Sum.py"
@pytest.fixture(scope="module")
def test_data():
    params_list = [
        [[1, 0, -1, 0, -2, 2], 0],
        [[1, 2, 3, 4], 0],
        [[-3, -2, -1, 0, 0, 1, 2, 3], 0],
        [[1, -2, -5, -4, -3, 3, 3, 5], -11],
        [[-497, -494, -484, -477, -453, -453, -444, -442, -428, -420, -401, -393, -392, -381, -357, -357, -327, -323,
          -306, -285, -284, -263, -262, -254, -243, -234, -208, -170, -166, -162, -158, -136, -133, -130, -119, -114,
          -101, -100, -86, -66, -65, -6, 1, 3, 4, 11, 69, 77, 78, 107, 108, 108, 121, 123, 136, 137, 151, 153, 155, 166,
          170, 175, 179, 211, 230, 251, 255, 266, 288, 306, 308, 310, 314, 321, 322, 331, 333, 334, 347, 349, 356, 357,
          360, 361, 361, 367, 375, 378, 387, 387, 408, 414, 421, 435, 439, 440, 441, 470, 492], 1682],
        [[-498, -492, -473, -455, -441, -412, -390, -378, -365, -359, -358, -326, -311, -305, -277, -265, -264, -256,
          -254, -240, -237, -234, -222, -211, -203, -201, -187, -172, -164, -134, -131, -91, -84, -55, -54, -52, -50,
          -27, -23, -4, 0, 4, 20, 39, 45, 53, 53, 55, 60, 82, 88, 89, 89, 98, 101, 111, 134, 136, 209, 214, 220, 221,
          224, 254, 281, 288, 289, 301, 304, 308, 318, 321, 342, 348, 354, 360, 383, 388, 410, 423, 442, 455, 457, 471,
          488, 488], -2808]
    ]
    res_list = [
        [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
        [],
        [[-3, -2, 2, 3], [-3, -1, 1, 3], [-3, 0, 0, 3], [-3, 0, 1, 2], [-2, -1, 0, 3], [-2, -1, 1, 2], [-2, 0, 0, 2],
         [-1, 0, 0, 1]],
        [[-5, -4, -3, 1]],
        [[306, 414, 470, 492], [310, 439, 441, 492], [314, 435, 441, 492], [331, 440, 441, 470], [333, 387, 470, 492],
         [333, 439, 440, 470], [334, 421, 435, 492], [347, 408, 435, 492], [356, 421, 435, 470], [357, 414, 441, 470],
         [361, 408, 421, 492], [367, 435, 439, 441], [387, 414, 440, 441], [387, 421, 435, 439], [408, 414, 421, 439]],
        []
    ]
    return params_list, res_list, 100


def test_018(test_data):
    func_test(Solution().fourSum, *test_data)


def test_018_2(test_data):
    func_test(Solution().fourSum2, *test_data)


def test_018_3(test_data):
    func_test(Solution().fourSum3, *test_data)


if __name__ == '__main__':
    # a = [-497, -494, -484, -477, -453, -453, -444, -442, -428, -420, -401, -393, -392, -381, -357, -357, -327, -323,
    #           -306, -285, -284, -263, -262, -254, -243, -234, -208, -170, -166, -162, -158, -136, -133, -130, -119, -114,
    #           -101, -100, -86, -66, -65, -6, 1, 3, 4, 11, 69, 77, 78, 107, 108, 108, 121, 123, 136, 137, 151, 153, 155, 166,
    #           170, 175, 179, 211, 230, 251, 255, 266, 288, 306, 308, 310, 314, 321, 322, 331, 333, 334, 347, 349, 356, 357,
    #           360, 361, 361, 367, 375, 378, 387, 387, 408, 414, 421, 435, 439, 440, 441, 470, 492], 1682
    # print(Solution().fourSum(*a))
    # print(sorted(Solution().fourSum3(*a)))
    pytest.main(['-vv', '--durations=10', '-q', '--tb=line', '-x', '018 4Sum.py'])

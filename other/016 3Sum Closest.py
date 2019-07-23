#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/3/10 20:19
# @File    : 016 3Sum Closest.py
# @Software: PyCharm

"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        closest = sum(nums[:3])
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                current = nums[i] + nums[j] + nums[k]
                if current == target:
                    return target
                if abs(current - target) < abs(closest - target):
                    closest = current
                if current < target:
                    j += 1
                else:
                    k -= 1
        return closest

    def threeSumClosest2(self, nums: List[int], target: int) -> int:
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        closest = sum(nums[:3])
        for i in range(len(nums) - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            min_sum = nums[i] + nums[i + 1] + nums[i + 2]
            max_sum = nums[i] + nums[-2] + nums[-1]
            if min_sum == target or max_sum == target:
                return target
            if min_sum > target:
                if abs(min_sum - target) < abs(closest - target):
                    closest = min_sum
                return closest
            if max_sum < target:
                if abs(max_sum - target) < abs(closest - target):
                    closest = max_sum
                continue
            j, k = i + 1, len(nums) - 1
            while j < k:
                current = nums[i] + nums[j] + nums[k]
                if current == target:
                    return target
                if abs(current - target) < abs(closest - target):
                    closest = current
                if current < target:
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                else:
                    k -= 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
        return closest


if __name__ == '__main__':
    print(Solution().threeSumClosest2([1, 1, 1, 1], 100))
    print(Solution().threeSumClosest2([1, 2, 4, 8, 16, 32, 64, 128], 82))

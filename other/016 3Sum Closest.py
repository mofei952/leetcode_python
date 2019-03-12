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
        """nums中和最接近target的三个数的和"""
        if len(nums) < 3:
            return 0
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        closest = sum(nums[:3])
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                if cur_sum == target:
                    return cur_sum
                if abs(cur_sum - target) < abs(closest - target):
                    closest = cur_sum
                if cur_sum > target:
                    k -= 1
                else:
                    j += 1
        return closest

    def threeSumClosest2(self, nums: List[int], target: int) -> int:
        """nums中和最接近target的三个数的和"""
        def closest_func(cur_sum):
            if cur_sum == target:
                return cur_sum
            if abs(cur_sum - target) < abs(closest - target):
                return cur_sum
            return closest
        if len(nums) < 3:
            return 0
        if len(nums) == 3:
            return sum(nums)
        nums.sort()
        closest = sum(nums[:3])
        for i in range(len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            if nums[i] + nums[k - 1] + nums[k] <= target:
                closest = closest_func(nums[i] + nums[k - 1] + nums[k])
            elif nums[i] + nums[j] + nums[j + 1] >= target:
                closest = closest_func(nums[i] + nums[j] + nums[j + 1])
            else:
                while j < k:
                    cur_sum = nums[i] + nums[j] + nums[k]
                    closest = closest_func(cur_sum)
                    if cur_sum > target:
                        k -= 1
                    else:
                        j += 1
            if closest == target:
                return target
        return closest


if __name__ == '__main__':
    result = Solution().threeSumClosest2([1, 2, 4, 8, 16, 32, 64, 128], 82)
    print(result)

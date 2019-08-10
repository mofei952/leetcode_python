#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/8/10 21:54
# @File    : 031 Next Permutation.py
# @Software: PyCharm

"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                # nums[i:]中 比nums[i-1]大的并且最接近nums[i-1], 和nums[i-1]交换位置
                closest_index = i
                for j in range(i, len(nums)):
                    if nums[j] > nums[i - 1]:
                        closest_index = j
                nums[closest_index], nums[i - 1] = nums[i - 1], nums[closest_index]
                # nums[i:]进行排序
                nums[i:] = sorted(nums[i:])
                break
        else:
            nums.reverse()


if __name__ == '__main__':
    print(Solution().nextPermutation([1, 3, 2]))

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/27 10:25
# @File    : 004 Median of Two Sorted Arrays.py
# @Software: PyCharm

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0

Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """查找两个有序列表重新排序后的中间值"""
        length = len(nums1) + len(nums2)
        if length % 2 == 0:
            return (self.find(nums1, nums2, length // 2) + self.find(nums1, nums2, length // 2 - 1)) / 2
        else:
            return self.find(nums1, nums2, length // 2)

    def find(self, nums1, nums2, k):
        """类似二分法查找两个列表的第k个值 O(log(m+n))"""
        m, n = len(nums1), len(nums2)
        t = k
        while t != 0:
            if m == 0:
                return nums2[t]
            elif n == 0:
                return nums1[t]
            elif nums1[m // 2] <= nums2[n // 2]:
                if t >= m // 2 + n // 2 + 1:
                    nums1 = nums1[m // 2 + 1:]
                    t -= m // 2 + 1
                    m = len(nums1)
                else:
                    nums2 = nums2[:n // 2]
                    n = len(nums2)
            else:
                nums1, nums2 = nums2, nums1
                m, n = n, m
        if m == 0:
            return nums2[t]
        elif n == 0:
            return nums1[t]
        return min(nums1[0], nums2[0])


if __name__ == '__main__':
    result = Solution().findMedianSortedArrays([1, 3], [2])
    print(result)

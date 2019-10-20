#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/11/20 20:00
# @File    : 056 Merge Intervals.py
# @Software: PyCharm

"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

from typing import List

from commons import running_time


class Solution(object):
    @running_time
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], cur[1])
            else:
                merged.append(cur)

        return merged

    @running_time
    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])

        merged = [intervals[0]]
        for i in range(1, len(intervals)):
            cur = intervals[i]
            if cur[0] > merged[-1][1]:
                merged.append(cur)
            elif cur[1] > merged[-1][1]:
                merged[-1][1] = cur[1]

        return merged


if __name__ == '__main__':
    assert Solution().merge([]) == []
    assert Solution().merge2([]) == []

    assert Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert Solution().merge2([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]

    assert Solution().merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert Solution().merge2([[1, 4], [4, 5]]) == [[1, 5]]

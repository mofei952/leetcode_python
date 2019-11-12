#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/10/20 13:59
# @File    : 057 Insert Interval.py
# @Software: PyCharm

"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

from typing import List

from commons import running_time


class Solution:
    @running_time
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        index = 0
        while index < len(intervals):
            cur = intervals[index]
            if cur[0] >= newInterval[0]:
                intervals.insert(index, newInterval)
                break
            index += 1
        else:
            intervals.append(newInterval)
        merged = []
        index = index or 1
        for j in range(index):
            merged.append(intervals[j])
        for j in range(index, len(intervals)):
            cur = intervals[j]
            if cur[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], cur[1])
            else:
                merged.append(cur)
        return merged

    @running_time
    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])

        merged = []
        for i, cur in enumerate(intervals):
            if merged and cur[0] <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], cur[1])
            else:
                merged.append(cur)
        return merged


if __name__ == '__main__':
    assert Solution().insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert Solution().insert2([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]

    assert Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
    assert Solution().insert2([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]

    assert Solution().insert([[2, 5], [6, 7], [8, 9]], [0, 1]) == [[0, 1], [2, 5], [6, 7], [8, 9]]
    assert Solution().insert2([[2, 5], [6, 7], [8, 9]], [0, 1]) == [[0, 1], [2, 5], [6, 7], [8, 9]]

"""
question:
https://leetcode.com/problems/non-overlapping-intervals/
"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        last_end = float('-inf')
        count = 0
        for start, end in intervals:
            if start < last_end:
                count += 1
            else:
                last_end = end
        return count


if __name__ == '__main__':
    assert Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
    assert Solution().eraseOverlapIntervals([[1, 2], [1, 3], [2, 3], [3, 4]]) == 1
    assert Solution().eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
    assert Solution().eraseOverlapIntervals([[1, 2], [2, 3]]) == 0

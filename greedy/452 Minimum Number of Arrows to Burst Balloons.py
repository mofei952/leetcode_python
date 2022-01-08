"""
question:
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
"""
from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        count = 1
        arrow_pos = points[0][1]
        for start, end in points:
            if arrow_pos < start:
                count += 1
                arrow_pos = end
        return count


if __name__ == '__main__':
    assert Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    assert Solution().findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
    assert Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
    assert Solution().findMinArrowShots([[1, 2]]) == 1
    assert Solution().findMinArrowShots([[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]) == 2

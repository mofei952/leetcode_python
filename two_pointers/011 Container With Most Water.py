"""
quesion:
https://leetcode.com/problems/container-with-most-water/

solution:
https://mofei952.github.io/2021/08/07/leetcode%2011%20Container%20With%20Most%20Water/
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0
        while i < j:
            if height[i] < height[j]:
                area = height[i] * (j - i)
                i += 1
            else:
                area = height[j] * (j - i)
                j -= 1
            max_area = max(max_area, area)
        return max_area

    def maxArea2(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0
        while i < j:
            if height[i] < height[j]:
                area = height[i] * (j - i)
                i += 1
            elif height[i] > height[j]:
                area = height[j] * (j - i)
                j -= 1
            else:
                area = height[j] * (j - i)
                i += 1
                j -= 1
            max_area = max(max_area, area)
        return max_area


if __name__ == '__main__':
    print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(Solution().maxArea2([1, 8, 6, 2, 5, 4, 8, 3, 7]))

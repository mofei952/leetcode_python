"""
quesion:
https://leetcode.com/problems/container-with-most-water/

solution:
https://blog.csdn.net/xingjingb/article/details/120107482
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
    assert Solution().maxArea2([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert Solution().maxArea2([1, 1]) == 1

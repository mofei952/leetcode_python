"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, 
find the area of largest rectangle in the histogram.

Example:
Input: [2,1,5,6,2,3]
Output: 10
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        if length == 0:
            return 0

        max_area = 0
        stack = [0]

        for i in range(1, length):
            height = heights[i]
            while stack and heights[stack[-1]] > height:
                h = heights[stack.pop()]
                w = i - 1 - stack[-1] if stack else i
                max_area = max(max_area, w * h)
            stack.append(i)

        while stack:
            h = heights[stack.pop()]
            w = length - 1 - stack[-1] if stack else length
            max_area = max(max_area, w * h)

        return max_area

    def largestRectangleArea2(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0

        max_area = 0
        stack = [-1, 0]
        heights.append(0)

        for i in range(1, len(heights)):
            height = heights[i]
            while heights[stack[-1]] > height:
                h = heights[stack.pop()]
                w = i - 1 - stack[-1]
                max_area = max(max_area, w * h)
            stack.append(i)

        return max_area


if __name__ == "__main__":
    print(Solution().largestRectangleArea2([2, 1, 5, 6, 2, 3]))
    print(Solution().largestRectangleArea2([1]))
"""
Given a 2D binary matrix filled with 0's and 1's, 
find the largest rectangle containing only 1's and return its area.

Example:
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""

from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        max_area = 0
        n = len(matrix[0])
        heights = [0] * (n + 1)

        for row in matrix:
            for j in range(n):
                heights[j] = 0 if row[j] == '0' else heights[j] + 1

            stack = [-1, 0]
            for i in range(1, n + 1):
                while heights[stack[-1]] > heights[i]:
                    h = heights[stack.pop()]
                    w = i - 1 - stack[-1]
                    max_area = max(max_area, w * h)
                stack.append(i)

        return max_area


if __name__ == "__main__":
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    print(Solution().maximalRectangle(matrix))

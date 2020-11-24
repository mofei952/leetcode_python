"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:
Input: 
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Output: 4
"""

from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        n = len(matrix)
        m = len(matrix[0])

        dp = [int(x) for x in matrix[0]]
        max_length = max(dp)

        for i in range(1, n):
            dp2 = [0] * m
            dp2[0] = int(matrix[i][0])
            max_length = max(max_length, dp2[0])
            for j in range(1, m):
                if matrix[i][j] == '0':
                    dp2[j] = 0
                else:
                    dp2[j] = min(dp[j-1], dp[j], dp2[j-1]) + 1
                    max_length = max(max_length, dp2[j])
            dp = dp2

        return max_length ** 2


if __name__ == "__main__":
    print(Solution().maximalSquare([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]))
    print(Solution().maximalSquare([
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]))
    print(Solution().maximalSquare([]))
    print(Solution().maximalSquare([
        ["1", "1"],
        ["1", "1"]
    ]))

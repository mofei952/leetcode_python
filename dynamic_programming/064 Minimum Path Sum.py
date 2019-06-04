#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/4 11:30
# @File    : 064 Minimum Path Sum.py
# @Software: PyCharm

"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        dp = [[0 for j in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                dp[i][j] = grid[i][j]
                if i and not j:
                    dp[i][j] += dp[i - 1][j]
                elif not i and j:
                    dp[i][j] += dp[i][j - 1]
                elif i and j:
                    dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
        return dp[row - 1][col - 1]

    def minPathSum2(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        dp = [0] * col
        dp[0] = grid[0][0]
        for i in range(1, len(dp)):
            dp[i] = dp[i - 1] + grid[0][i]
        for i in range(1, row):
            dp[0] += grid[i][0]
            for j in range(1, col):
                dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]
        return dp[-1]


if __name__ == '__main__':
    print(Solution().minPathSum2([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]))
    print(Solution().minPathSum2([[1]]))

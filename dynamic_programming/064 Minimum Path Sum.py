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
        m = len(grid)
        n = len(grid[0])

        dp = [0] * n

        dp[0] = grid[0][0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + grid[0][i]

        for i in range(1, m):
            dp[0] = dp[0] + grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j - 1], dp[j]) + grid[i][j]

        return dp[-1]


if __name__ == '__main__':
    print(Solution().minPathSum([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]))
    print(Solution().minPathSum([[1]]))

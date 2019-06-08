#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/4 21:34
# @File    : 063 Unique Paths II.py
# @Software: PyCharm


"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.
Note: m and n will be at most 100.

Example 1:
Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2

Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
"""

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[1 for j in range(m)] for i in range(n)]
        dp[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, n):
            dp[i][0] = 0 if obstacleGrid[i][0] else dp[i - 1][0]
        for j in range(1, m):
            dp[0][j] = 0 if obstacleGrid[0][j] else dp[0][j - 1]
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = 0 if obstacleGrid[i][j] else dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid:
            return 0
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [0] * m
        dp[0] = 1
        for i in range(n):
            dp[0] = 0 if obstacleGrid[i][0] else dp[0]
            for j in range(1, m):
                dp[j] = 0 if obstacleGrid[i][j] else dp[j - 1] + dp[j]
        return dp[-1]


if __name__ == '__main__':
    print(Solution().uniquePathsWithObstacles([[1, 0]]))
    print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))

    print(Solution().uniquePathsWithObstacles2([[1, 0]]))
    print(Solution().uniquePathsWithObstacles2([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))

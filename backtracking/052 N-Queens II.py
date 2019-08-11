#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/17 19:36
# @File    : 052 N-Queens II.py
# @Software: PyCharm

"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:
Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""


class Solution:
    def totalNQueens(self, n: int) -> int:
        def recursive(i):
            total = 0
            if n == i:
                return 1
            for j in range(n):
                if j not in cols and j - i not in diffs and j + i not in sums:
                    cols.add(j)
                    diffs.add(j - i)
                    sums.add(j + i)
                    total += recursive(i + 1)
                    cols.remove(j)
                    diffs.remove(j - i)
                    sums.remove(j + i)
            return total
        cols = set()
        diffs = set()
        sums = set()
        total = recursive(0)
        return total


if __name__ == '__main__':
    for i in range(11):
        res = Solution().totalNQueens(i)
        print(res)

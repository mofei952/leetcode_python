#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/16 18:43
# @File    : 051 N-Queens.py
# @Software: PyCharm

"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:
Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def recursive(i):
            if n == i:
                res.append(list(board))
            for j in range(n):
                if j not in cols and j - i not in diffs and j + i not in sums:
                    # board.append(''.join('Q' if k == j else '.' for k in range(n)))
                    board.append('.' * j + 'Q' + '.' * (n - j - 1))
                    cols.add(j)
                    diffs.add(j - i)
                    sums.add(j + i)
                    recursive(i + 1)
                    board.pop()
                    cols.remove(j)
                    diffs.remove(j - i)
                    sums.remove(j + i)

        res = []
        board = []
        cols = set()
        diffs = set()
        sums = set()
        recursive(0)
        return res


if __name__ == '__main__':
    print(Solution().solveNQueens(4))

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/12/1 12:14
# @File    : 059 Spiral Matrix II.py
# @Software: PyCharm

"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.

Example:
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return []

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_index = 0
        x, y = 0, -1
        num = 1
        matrix = [[0] * n for i in range(n)]

        for i in range(n * n):
            dx, dy = dirs[dir_index]
            x, y = x + dx, y + dy
            matrix[x][y] = num
            num += 1

            xx, yy = x + dx, y + dy
            if xx < 0 or xx >= n or yy < 0 or yy >= n or matrix[xx][yy]:
                dir_index = (dir_index + 1) % 4

        return matrix

    def generateMatrix2(self, n: int) -> List[List[int]]:
        if not n:
            return []

        matrix = [[0] * n for i in range(n)]

        row_start, row_end = 0, n - 1
        col_start, col_end = 0, n - 1

        num = 1
        while row_start <= row_end and col_start <= col_end:
            for i in range(col_start, col_end + 1):
                matrix[row_start][i] = num
                num += 1
            row_start += 1

            for i in range(row_start, row_end + 1):
                matrix[i][col_end] = num
                num += 1
            col_end -= 1

            if row_start <= row_end:
                for i in range(col_end, col_start - 1, -1):
                    matrix[row_end][i] = num
                    num += 1
                row_end -= 1

            if col_start <= col_end:
                for i in range(row_end, row_start - 1, -1):
                    matrix[i][col_start] = num
                    num += 1
                col_start += 1

        return matrix


if __name__ == '__main__':
    result = Solution().generateMatrix(10)
    for line in result:
        print([format(i, '3d') for i in line])

    result = Solution().generateMatrix2(10)
    for line in result:
        print([format(i, '3d') for i in line])

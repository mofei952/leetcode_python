#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/10/16 20:49
# @File    : 054 Spiral Matrix.py
# @Software: PyCharm

"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

from typing import List

from commons import running_time


class Solution:
    @running_time
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_index = 0
        x, y = 0, -1
        n, m = len(matrix), len(matrix[0])
        visit = [[0] * m for i in range(n)]

        order = []
        for i in range(n * m):
            dx, dy = dirs[dir_index]
            x, y = x + dx, y + dy
            order.append(matrix[x][y])
            visit[x][y] = 1

            xx, yy = x + dx, y + dy
            if xx < 0 or xx >= n or yy < 0 or yy >= m or visit[xx][yy]:
                dir_index = (dir_index + 1) % 4

        return order

    @running_time
    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        row, col = 0, -1
        n, m = len(matrix), len(matrix[0])
        rows, cols = n - 1, m
        speed = 1

        pos_list = []
        while len(pos_list) < n * m:
            for i in range(cols):
                col += speed
                pos_list.append((row, col))

            for i in range(rows):
                row += speed
                pos_list.append((row, col))

            speed = -speed
            rows -= 1
            cols -= 1

        return [matrix[x][y] for x, y in pos_list]

    @running_time
    def spiralOrder3(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        n, m = len(matrix), len(matrix[0])
        row_start, row_end = 0, n - 1
        col_start, col_end = 0, m - 1

        result = []
        while row_start <= row_end and col_start <= col_end:
            for i in range(col_start, col_end + 1):
                result.append(matrix[row_start][i])
            row_start += 1

            for i in range(row_start, row_end + 1):
                result.append(matrix[i][col_end])
            col_end -= 1

            if row_start <= row_end:
                for i in range(col_end, col_start - 1, -1):
                    result.append(matrix[row_end][i])
                row_end -= 1

            if col_start <= col_end:
                for i in range(row_end, row_start - 1, -1):
                    result.append(matrix[i][col_start])
                col_start += 1

        return result


if __name__ == '__main__':
    list_ = [
    ]
    assert Solution().spiralOrder(list_) == []
    assert Solution().spiralOrder2(list_) == []
    assert Solution().spiralOrder3(list_) == []

    list_ = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert Solution().spiralOrder(list_) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert Solution().spiralOrder2(list_) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert Solution().spiralOrder3(list_) == [1, 2, 3, 6, 9, 8, 7, 4, 5]

    list_ = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    assert Solution().spiralOrder(list_) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert Solution().spiralOrder2(list_) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert Solution().spiralOrder3(list_) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

    list_ = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16],
        [17, 18, 19, 20]
    ]
    assert Solution().spiralOrder(list_) == [1, 2, 3, 4, 8, 12, 16, 20, 19, 18, 17, 13, 9, 5, 6, 7, 11, 15, 14, 10]
    assert Solution().spiralOrder2(list_) == [1, 2, 3, 4, 8, 12, 16, 20, 19, 18, 17, 13, 9, 5, 6, 7, 11, 15, 14, 10]
    assert Solution().spiralOrder3(list_) == [1, 2, 3, 4, 8, 12, 16, 20, 19, 18, 17, 13, 9, 5, 6, 7, 11, 15, 14, 10]

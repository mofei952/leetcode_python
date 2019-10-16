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


class Solution:
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


if __name__ == '__main__':
    list_ = [
    ]
    print(Solution().spiralOrder(list_))
    print(Solution().spiralOrder2(list_))

    list_ = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(Solution().spiralOrder(list_))
    print(Solution().spiralOrder2(list_))

    list_ = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print(Solution().spiralOrder(list_))
    print(Solution().spiralOrder2(list_))

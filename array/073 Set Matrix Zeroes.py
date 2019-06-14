#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/13 21:40
# @File    : 073 Set Matrix Zeroes.py
# @Software: PyCharm

"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:
Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:
Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
"""

import random
from typing import List

import pytest

from commons import func_test


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        n = len(matrix)
        m = len(matrix[0])
        rows = set()
        cols = set()
        for i in range(n):
            for j in range(m):
                if not matrix[i][j]:
                    rows.add(i)
                    cols.add(j)
        for i in rows:
            for j in range(m):
                matrix[i][j] = 0
        for j in cols:
            for i in range(n):
                matrix[i][j] = 0

    def setZeroes2(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        n = len(matrix)
        m = len(matrix[0])
        rows = set()
        cols = set()
        for i in range(n):
            for j in range(m):
                if not matrix[i][j]:
                    rows.add(i)
                    cols.add(j)
        for i in range(n):
            for j in range(m):
                if i in rows or j in cols:
                    matrix[i][j] = 0


@pytest.fixture(scope="module")
def test_data():
    params_list = [
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]],),
        ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],),
    ]
    res_list = [
        None,
        None
    ]
    for i in range(3, 20):
        param = [[random.randint(0, i) for _ in range(i)] for _ in range(i)]
        params_list.append((param,))
        res_list.append(None)
    return params_list, res_list, 1000


def test_73(test_data):
    func_test(Solution().setZeroes, *test_data)


def test_73_2(test_data):
    func_test(Solution().setZeroes2, *test_data)


if __name__ == '__main__':
    pytest.main(['-vv', '--durations=10', '-q', '--tb=line', '-x', '073 Set Matrix Zeroes.py'])
    # data = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    # Solution().setZeroes(data)
    # for i in data:
    #     print(i)

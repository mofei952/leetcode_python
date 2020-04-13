#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/4/13 20:17
# @File    : 074 Search a 2D Matrix.py
# @Software: PyCharm

"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""

from typing import List

import pytest

from commons import func_test


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m = len(matrix)
        n = len(matrix[0])

        low, high = 0, m * n - 1
        while low <= high:
            mid = (low + high) // 2
            num = matrix[mid // n][mid % n]
            if num == target:
                return True
            elif num > target:
                high = mid - 1
            else:
                low = mid + 1
        return False

    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        low, high = 0, m - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][-1] < target:
                low = mid + 1
            else:
                low = mid
                break

        if low >= m:
            return False

        row = low
        arr = matrix[row]

        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] > target:
                high = mid - 1
            elif arr[mid] < target:
                low = mid + 1
            else:
                return True
        return False

    def binarySearch(self, arr, target):
        low, high = 0, len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return low


@pytest.fixture(scope="module")
def test_data():
    params_list = []
    res_list = []

    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    for i in range(-5, 55):
        params_list.append((matrix, i))
        res_list.append(Solution().searchMatrix(matrix, i))

    return params_list, res_list, 10000


def test_74(test_data):
    func_test(Solution().searchMatrix, *test_data)


def test_74_2(test_data):
    func_test(Solution().searchMatrix2, *test_data)


if __name__ == '__main__':
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    for i in range(-1, 53):
        # print(i, Solution().searchMatrix(matrix, i) == Solution().searchMatrix2(matrix, i))
        assert Solution().searchMatrix(matrix, i) == Solution().searchMatrix2(matrix, i)

    pytest.main(['--durations=10', '074 Search a 2D Matrix.py'])

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/12 18:38
# @File    : 120 Triangle.py
# @Software: PyCharm

"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

import random
from typing import List

import pytest

from commons import func_test


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[0 for j in range(len(triangle[i]))] for i in range(len(triangle))]
        dp[0][0] = triangle[0][0]
        for i in range(1, len(dp)):
            dp[i][0] = triangle[i][0] + dp[i - 1][0]
            dp[i][-1] = triangle[i][-1] + dp[i - 1][-1]
            for j in range(1, len(dp[i]) - 1):
                dp[i][j] = triangle[i][j] + min(dp[i - 1][j - 1], dp[i - 1][j])
        return min(dp[-1])

    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        dp = [v for v in triangle[-1]]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]

    def minimumTotal3(self, triangle: List[List[int]]) -> int:
        dp = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(i + 1):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]


@pytest.fixture(scope="module")
def test_data():
    params_list = [
        ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]],),
        ([[-1], [3, 2], [-3, 1, -1]],),
    ]
    res_list = [
        11,
        -1
    ]
    # 模拟1-20层的参数各100个
    for i in range(1, 41):
        for _ in range(100):
            param = [[random.randint(-10, 90) for k in range(j + 1)] for j in range(i)]
            params_list.append((param,))
            res_list.append(Solution().minimumTotal(param))
    return params_list, res_list, 1


def test_120(test_data):
    func_test(Solution().minimumTotal, *test_data)


def test_120_2(test_data):
    func_test(Solution().minimumTotal2, *test_data)


def test_120_3(test_data):
    func_test(Solution().minimumTotal3, *test_data)


if __name__ == '__main__':
    # print(Solution().minimumTotal([[2], [7, 8], [18, 17, 21], [33, 28, 35, 37]]))
    # print(Solution().minimumTotal4([[2], [7, 8], [18, 17, 21], [33, 28, 35, 37]]))
    pytest.main(['-vv', '--durations=10', '-q', '--tb=line', '-x', 'dynamic_programming/120 Triangle.py'])

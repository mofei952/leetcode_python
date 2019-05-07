#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/7 20:52
# @File    : 343 Integer Break.py
# @Software: PyCharm

"""
Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers.
Return the maximum product you can get.

Example 1:
Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.

Example 2:
Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

Note: You may assume that n is not less than 2 and not larger than 58.
"""
import pytest

from commons import func_test


class Solution:
    def integerBreak(self, n: int) -> int:
        m = -1
        for i in range(2, n + 1):
            t = round(n / i)
            s = t ** (i - 1) * (n - t * (i - 1))
            if s > m:
                m = s
        return m

    def integerBreak2(self, n: int) -> int:
        if n <= 7:
            b = 2
        else:
            b = (n + 1) // 3
        t = round(n / b)
        s = t ** (b - 1) * (n - t * (b - 1))
        return s

    def integerBreak3(self, n: int) -> int:
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n % 3 == 0:
            return 3 ** (n // 3)
        if n % 3 == 1:
            return 3 ** (n // 3 - 1) * 4
        if n % 3 == 2:
            return 3 ** (n // 3) * 2
        return 0


@pytest.fixture(scope="module")
def test_data():
    params_list = []
    res_list = []
    for i in range(2, 59):
        params_list.append((i,))
        res_list.append(Solution().integerBreak(i))
    return params_list, res_list, 1000


def test_343(test_data):
    func_test(Solution().integerBreak, *test_data)


def test_343_2(test_data):
    func_test(Solution().integerBreak2, *test_data)


def test_343_3(test_data):
    func_test(Solution().integerBreak3, *test_data)


if __name__ == '__main__':
    pytest.main(['-vv', '--durations=10', '-q', '--tb=line', '-x', '343 Integer Break.py'])
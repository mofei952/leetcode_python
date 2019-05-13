#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/11 12:09
# @File    : 50 Pow(x, n).py
# @Software: PyCharm

"""
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Example 2:
Input: 2.10000, 3
Output: 9.26100

Example 3:
Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25

Note:
-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
"""
import random

import math
import pytest

from commons import func_test


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        s = self.myPow(x, n // 2)
        s = s * s

        if n % 2 == 1:
            s *= x

        return s

    def myPow2(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        arr = []
        while n:
            arr.append(n % 2)
            n //= 2

        s = x
        arr = arr[:-1]
        for i in arr[::-1]:
            s = s * s
            if i == 1:
                s = s * x

        return s

    def myPow3(self, x: float, n: int) -> float:
        if not n:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        arr = bin(n)[3:]

        s = x
        for i in arr:
            s = s * s
            if i == '1':
                s = s * x

        return s

    def myPow4(self, x, n):
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        ans = 1
        while n:
            if n & 1:
                ans *= x
            x *= x
            n >>= 1

        return ans


@pytest.fixture(scope="module")
def test_data():
    params_list = [
        (2.00000, -2147483648),
        (0.00001, 2147483647),
        (2.100, 3),
        (2.000, -2),
    ]
    res_list = [
        0.0,
        0.0,
        9.261000000000001,
        0.25,
    ]
    for i in range(-2147483648, 2147483649, random.randint(15000, 22000)):
        a, b = round(random.random() * 20, 5), i
        try:
            res_list.append(math.pow(a, b))
            params_list.append((a, b))
        except:
            pass
    return params_list, res_list, 1


def test_50_pow(test_data):
    func_test(math.pow, *test_data)


def test_50_1(test_data):
    func_test(Solution().myPow, *test_data)


def test_50_2(test_data):
    func_test(Solution().myPow2, *test_data)


def test_50_3(test_data):
    func_test(Solution().myPow3, *test_data)


def test_50_4(test_data):
    func_test(Solution().myPow3, *test_data)


if __name__ == '__main__':
    pytest.main(['-vv', '--durations=10', '-q', '--tb=line', '-x', '050 Pow(x, n).py'])

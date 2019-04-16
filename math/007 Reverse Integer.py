#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/27 15:28
# @File    : 007 Reverse Integer.py
# @Software: PyCharm

"""
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21

Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2**31,  2**31 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""
import pytest

from commons import func_test


class Solution:
    def reverse(self, x: int) -> int:
        """反转整型变量的数字"""
        sign = -1 if x < 0 else 1
        x *= sign
        res = 0
        while x:
            t = x % 10
            x //= 10
            res = res * 10 + t
        if not -2 ** 31 <= res <= 2 ** 31 - 1:
            return 0
        return res * sign

    def reverse2(self, x):
        """反转整型变量的数字， 通过转换为字符串再反转实现"""
        sign = -1 if x < 0 else 1
        x *= sign
        s = str(x)
        res = 0
        for i in s[::-1]:
            res = res * 10 + (ord(i) - ord('0'))
        res *= sign
        if res < -2 ** 31 or res > 2 ** 31 - 1:
            return 0
        return res


@pytest.fixture(scope="module")
def test_data():
    params_list = [
        (123,),
        (-123,),
        (120,),
        (1534236469,),
    ]
    res_list = [
        321,
        -321,
        21,
        0,
    ]
    for i in range(-100000, 299999):
        params_list.append((i,))
        res_list.append(Solution().reverse(i))
    return params_list, res_list, 1


def test_007(test_data):
    func_test(Solution().reverse, *test_data)


def test_007_2(test_data):
    func_test(Solution().reverse2, *test_data)


if __name__ == '__main__':
    pytest.main(['-vv', '--durations=10', '-q', '--tb=line', '-x', '007 Reverse Integer.py'])

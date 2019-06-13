#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/13 19:11
# @File    : 067 Add Binary.py
# @Software: PyCharm

"""
Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
"""
import random

import pytest

from commons import func_test


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary2(self, a: str, b: str) -> str:
        if len(b) < len(a):
            a, b = b, a
        diff = len(b) - len(a)
        res = ''
        c = 0
        for i in range(len(a) - 1, -1, -1):
            s = c + int(a[i]) + int(b[i + diff])
            res += str(s % 2)
            c = s // 2
        for j in range(diff - 1, -1, -1):
            s = c + int(b[j])
            res += str(s % 2)
            c = s // 2
        if c:
            res += str(c)
        return res[::-1]


@pytest.fixture(scope="module")
def test_data():
    params_list = [
        ('11', '1'),
        ('1010', '1011'),
    ]
    res_list = [
        '100',
        '10101'
    ]
    for i in range(1, 20):
        for j in range(1, 20):
            params = []
            params.append('1' + ''.join(str(random.randint(0, 1)) for _ in range(i)))
            params.append('1' + ''.join(str(random.randint(0, 1)) for _ in range(j)))
            params_list.append(params)
            print(params)
            res_list.append(Solution().addBinary(*params))
    return params_list, res_list, 100


def test_67(test_data):
    func_test(Solution().addBinary, *test_data)


def test_67_2(test_data):
    func_test(Solution().addBinary2, *test_data)


if __name__ == '__main__':
    # print(Solution().addBinary('11', '1'))
    # print(Solution().addBinary('1010', '1011'))
    pytest.main(['-vv', '--durations=10', '-q', '--tb=line', '-x', '067 Add Binary.py'])

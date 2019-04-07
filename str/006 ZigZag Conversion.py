#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/27 14:23
# @File    : 006 ZigZag Conversion.py
# @Software: PyCharm

"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
"""

from collections import defaultdict

import pytest

from commons import func_test


class Solution:

    def convert(self, s: str, numRows: int) -> str:
        """z形状列表转换为正常显示, 通过分别统计每行的字母实现"""
        if numRows == 0:
            return ''
        if numRows == 1:
            return s
        dict_ = {}
        row = 1
        step = 1
        for v in s:
            if row not in dict_:
                dict_[row] = []
            dict_[row].append(v)
            row += step
            if row == 1 or row == numRows:
                step *= -1
        result = ''
        for i in range(1, numRows + 1):
            if i in dict_:
                result += ''.join(dict_[i])
        return result

    def convert2(self, s: str, numRows: int) -> str:
        if numRows == 0:
            return ''
        if numRows == 1:
            return s
        line = 1
        speed = 1
        dict_ = defaultdict(list)
        for v in s:
            dict_[line].append(v)
            line += speed
            if line == numRows or line == 1:
                speed = -speed
        res = ''
        for i in range(1, numRows + 1):
            res += ''.join(dict_[i])
        return res


# pytest -vv --durations=10 -q --tb=line "str\006 ZigZag Conversion.py"
@pytest.fixture(scope="module")
def test_data():
    params_list = [
        ('PAYPALISHIRING', 3),
        ('PAYPALISHIRING', 4),
    ]
    res_list = [
        'PAHNAPLSIIGYIR',
        'PINALSIGYAHRPI',
    ]
    return params_list, res_list, 100000


def test_06(test_data):
    func_test(Solution().convert, *test_data)


def test_06_2(test_data):
    func_test(Solution().convert2, *test_data)

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/3 19:51
# @File    : 066 Plus One.py
# @Software: PyCharm

from typing import List

import pytest

from commons import func_test

"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.
The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.
You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = 0
        for num in digits:
            s = s * 10 + num
        s += 1
        res = []
        while s:
            res.append(s % 10)
            s //= 10
        return res[::-1]

    def plusOne2(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                break
            digits[i] = 0
        else:
            digits.insert(0, 1)
        return digits


@pytest.fixture(scope="module")
def test_data():
    params_list = [
        ([1, 2, 3],),
        ([1, 9, 9, 9],),
        ([9, 9, 9, 9],),
    ]
    res_list = [
        [1, 2, 4],
        [2, 0, 0, 0],
        [1, 0, 0, 0, 0],
    ]
    for i in range(100000):
        t = list(map(int, list(str(i))))
        print(t)
        params_list.append((t,))
        res_list.append(Solution().plusOne(t))
    return params_list, res_list, 1


def test_50_pow(test_data):
    func_test(Solution().plusOne, *test_data)


def test_50_pow_2(test_data):
    func_test(Solution().plusOne2, *test_data)


if __name__ == '__main__':
    pytest.main(['-vv', '--durations=10', '-q', '--tb=line', '-x', '066 Plus One.py'])

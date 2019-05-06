#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/6 17:26
# @File    : 172 Factorial Trailing Zeroes.py
# @Software: PyCharm

"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
"""
import pytest

from commons import func_test


class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 每个数字5会产生一个尾数0，25产生两个，以此类推...
        count = 0
        i = 5
        while n >= i:
            count += n // i
            i *= 5
        return count


@pytest.fixture(scope="module")
def test_data():
    params_list = [
        (3,),
        (5,),
        (6,),
        (25,),
        (8401,),
    ]
    res_list = [
        0,
        1,
        1,
        6,
        2098,
    ]
    return params_list, res_list, 100000


def test_172(test_data):
    func_test(Solution().trailingZeroes, *test_data)


if __name__ == '__main__':
    pytest.main(['-vv', '--durations=10', '-q', '--tb=line', '-x', '172 Factorial Trailing Zeroes.py'])

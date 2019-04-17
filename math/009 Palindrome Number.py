#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/28 14:35
# @File    : 009 Palindrome Number.py
# @Software: PyCharm

"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
"""
import random

import pytest

from commons import func_test


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """是否回文数字, Runtime: 76 ms, faster than 100.00% of Python3 online submissions for Palindrome Number."""
        if x < 0:
            return False
        if x < 10:
            return True
        s = str(x)
        return s[::-1] == s

    def isPalindrome2(self, x: int) -> bool:
        """是否回文数字"""
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False
        reverse = 0
        t = x
        while t:
            reverse = reverse * 10 + t % 10
            if reverse > x:
                return False
            t //= 10
        return reverse == x


@pytest.fixture(scope="module")
def test_data():
    params_list = [
        (121,),
        (-121,),
        (10,),
        (10000000000000000000000000000000,),
    ]
    res_list = [
        True,
        False,
        False,
        False
    ]
    for i in range(-1000, 2999999):
        v = i * 100000 + random.randint(1, 99999)
        params_list.append((v,))
        res_list.append(Solution().isPalindrome(v))
    return params_list, res_list, 1


def test_007(test_data):
    func_test(Solution().isPalindrome, *test_data)


def test_007_2(test_data):
    func_test(Solution().isPalindrome2, *test_data)


if __name__ == '__main__':
    pytest.main(['-vv', '--durations=10', '-q', '--tb=line', '-x', '009 Palindrome Number.py'])
    # pytest.main(['-x', '009 Palindrome Number.py'])

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/15 23:19
# @File    : 028 Implement strStr().py
# @Software: PyCharm

"""
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string.
This is consistent to C's strstr() and Java's indexOf().
"""
import pytest

from commons import func_test


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """查找第一次出现needle的位置"""
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1

    def strStr2(self, haystack: str, needle: str) -> int:
        """查找第一次出现needle的位置"""
        if not needle:
            return 0
        if len(haystack) < len(needle):
            return -1
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


# pytest -q --tb=line "str\028 Implement strStr().py"
# pytest -vv --durations=10 -q --tb=line "str\028 Implement strStr().py"
@pytest.fixture(scope="module")
def test_data():
    params_list = [
        ('hello', ''),
        ('hello', 'hello aa'),
        ('hello', 'll'),
        ('hello', 'lo'),
        ('hello', 'aa'),
        ('hello', 'dd')
    ]
    res_list = [
        0,
        -1,
        2,
        3,
        -1,
        -1
    ]
    return params_list, res_list, 100000


def test_028(test_data):
    func_test(Solution().strStr, *test_data)


def test_028_2(test_data):
    func_test(Solution().strStr2, *test_data)


if __name__ == '__main__':
    pytest.main(['-vv', '--durations=10', '-q', '--tb=line', '028 Implement strStr().py'])

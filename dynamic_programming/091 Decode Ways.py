#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/11 20:09
# @File    : 091 Decode Ways.py
# @Software: PyCharm

"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""

import pytest

from commons import func_test


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        dp = [0] * len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            if 1 <= int(s[i]):
                dp[i] = dp[i - 1]
            if 10 <= int(s[i - 1] + s[i]) <= 26:
                dp[i] += dp[i - 2] if i >= 2 else 1
        # print(dp)
        return dp[-1]

    def numDecodings2(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = dp[1] = 1
        for i in range(1, len(s)):
            if s[i] != '0':
                dp[i + 1] += dp[i]
            if 10 <= int(s[i - 1] + s[i]) <= 26:
                dp[i + 1] += dp[i - 1]
        return dp[-1]


@pytest.fixture(scope="module")
def test_data():
    params_list = [
        ('0',),
        ('1',),
        ('01',),
        ('10',),
        ('12',),
        ('226',),
        ('27',),
        ('101',),
    ]
    res_list = [
        0,
        1,
        0,
        1,
        2,
        3,
        1,
        1,
    ]
    for i in range(1000, 5555555, 12314):
        p = str(i)
        params_list.append((p,))
        res_list.append(Solution().numDecodings(p))
    return params_list, res_list, 500


def test_91(test_data):
    func_test(Solution().numDecodings, *test_data)


def test_91_2(test_data):
    func_test(Solution().numDecodings2, *test_data)


if __name__ == '__main__':
    pytest.main(['-vv', '--durations=10', '-q', '--tb=line', '-x', '091 Decode Ways.py'])
    # print(Solution().numDecodings('0'))
    # print(Solution().numDecodings('1'))
    # print(Solution().numDecodings('01'))
    # print(Solution().numDecodings('10'))
    # print(Solution().numDecodings('12'))
    # print(Solution().numDecodings('226'))
    # print(Solution().numDecodings('27'))
    # print(Solution().numDecodings('101'))

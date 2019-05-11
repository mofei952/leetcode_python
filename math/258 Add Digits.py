#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/11 10:56
# @File    : 258 Add Digits.py
# @Software: PyCharm

"""
Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:
Input: 38
Output: 2
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2.
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?
"""


class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            t = 0
            while num:
                t += num % 10
                num //= 10
            num = t
        return num


if __name__ == '__main__':
    print(Solution().addDigits(38))

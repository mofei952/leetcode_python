#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/4/21 16:31
# @File    : 202 Happy Number.py
# @Software: PyCharm

"""
Write an algorithm to determine if a number is "happy".
A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example:
Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        if n <= 0:
            return False
        record = set()
        while True:
            m = 0
            while n:
                m += (n % 10) ** 2
                n //= 10
            if m == 1:
                return True
            if m in record:
                return False
            record.add(m)
            n = m


if __name__ == '__main__':
    print(Solution().isHappy(7))

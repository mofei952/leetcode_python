#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/30 20:30
# @File    : 43 Multiply Strings.py
# @Software: PyCharm

"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Note:
1. The length of both num1 and num2 is < 110.
2. Both num1 and num2 contain only digits 0-9.
3. Both num1 and num2 do not contain any leading zero, except the number 0 itself.
4. You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


class Solution:
    def str_to_int(self, s):
        val = 0
        for n in s:
            val = val * 10 + ord(n) - ord('0')
        return val

    def multiply(self, num1: str, num2: str) -> str:
        res = self.str_to_int(num1) * self.str_to_int(num2)
        return str(res)


if __name__ == '__main__':
    print(Solution().multiply('123', '456'))

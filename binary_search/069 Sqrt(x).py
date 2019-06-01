#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/1 12:03
# @File    : 69 Sqrt(x).py
# @Software: PyCharm

"""
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        i = x
        while i >= 0 and i * i > x:
            i -= 1
        return i

    def mySqrt2(self, x: int) -> int:
        low = 0
        high = x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                low = mid + 1
            else:
                high = mid - 1
        return high


if __name__ == '__main__':
    a = [0] * 30
    for i in range(0, 500):
        res = Solution().mySqrt2(i)
        a[res] += 1
        # print(i, res)
    print(a)

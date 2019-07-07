#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/7/7 11:58
# @File    : 038 Count and Say.py
# @Software: PyCharm


"""
The count-and-say sequence is the sequence of integers with the first five terms as following:
1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
Note: Each term of the sequence of integers will be represented as a string.

Example 1:
Input: 1
Output: "1"

Example 2:
Input: 4
Output: "1211"
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        current = '1'
        for i in range(1, n):
            count = 1
            next = ''
            for j in range(1, len(current)):
                if current[j] == current[j - 1]:
                    count += 1
                else:
                    next += str(count) + current[j - 1]
                    count = 1
            next += str(count) + current[-1]
            current = next
        return current


if __name__ == '__main__':
    for i in range(1, 11):
        print(Solution().countAndSay(i))

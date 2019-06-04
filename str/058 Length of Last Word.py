#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/30 20:36
# @File    : 58 Length of Last Word.py
# @Software: PyCharm

"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.
If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:
Input: "Hello World"
Output: 5
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1
        while end >= 0 and s[end] == ' ':
            end -= 1
        i = end
        while i >= 0 and s[i] != ' ':
            i -= 1
        return end - i


if __name__ == '__main__':
    print(Solution().lengthOfLastWord('hello world'))
    print(Solution().lengthOfLastWord(''))

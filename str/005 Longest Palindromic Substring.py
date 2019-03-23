#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/27 12:12
# @File    : 005 Longest Palindromic Substring.py
# @Software: PyCharm

"""
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """最长回文子串"""
        if not s:
            return ''
        result = s[0]
        for i in range(len(s)):
            if min(i, len(s) - i - 1) * 2 + 1 > len(result):
                ss = self.longest_palindrome_from_center(s, i - 1, i + 1)
                if len(ss) > len(result):
                    result = ss
            if i + 1 < len(s) and s[i] == s[i + 1]:
                if min(i, len(s) - i - 2) * 2 + 2 > len(result):
                    ss = self.longest_palindrome_from_center(s, i - 1, i + 2)
                    if len(ss) > len(result):
                        result = ss
        return result

    def longest_palindrome_from_center(self, s, l, r):
        while l >= 0 and r < len(s):
            if s[l] == s[r]:
                l -= 1
                r += 1
            else:
                break
        return s[l + 1: r]


if __name__ == '__main__':
    result = Solution().longestPalindrome('aaa12aaadsafasf')
    print(result)

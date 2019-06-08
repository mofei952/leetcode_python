#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/8 22:22
# @File    : 072 Edit Distance.py
# @Software: PyCharm

"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
You have the following 3 operations permitted on a word:
Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if not n:
            return m
        if not m:
            return n
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                t = 0 if word1[i - 1] == word2[j - 1] else 1
                dp[i][j] = min(dp[i - 1][j - 1] + t, dp[i][j - 1] + 1, dp[i - 1][j] + 1)
        # for row in dp:
        #     print(row)
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().minDistance('horse', 'ros'))
    print(Solution().minDistance('intention', 'execution'))
    print(Solution().minDistance('', ''))
    print(Solution().minDistance('a', 'b'))
    print(Solution().minDistance("pneumonoultramicroscopicsilicovolcanoconiosis", "ultramicroscopically"))

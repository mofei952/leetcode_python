"""
Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:
Input: s = "a"
Output: [["a"]]
"""

from typing import List
from functools import lru_cache
from collections import defaultdict


class Solution:

    def partition(self, s: str) -> List[List[str]]:
        dp = [[] for _ in range(len(s))]
        dp.insert(0, [[]])
        for i in range(1, len(s)+1):
            for j in range(i-1, -1, -1):
                t = s[j: i]
                if t == t[::-1]:
                    dp[i].extend([d+[t] for d in dp[j]])
        return dp[-1]


if __name__ == '__main__':
    print(Solution().partition('aab'))

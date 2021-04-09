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


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [tuple([s])]
        res = []
        if ''.join(reversed(s)) == s:
            res.append(tuple([s]))
        for i in range(1, len(s)):
            r1 = self.partition(s[0: i])
            r2 = self.partition(s[i: len(s)])
            res.extend([tuple(t1 + t2) for t1 in r1 for t2 in r2])
        return list(set(res))


if __name__ == '__main__':
    print(Solution().partition('aab'))

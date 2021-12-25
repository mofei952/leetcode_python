"""
question:
https://leetcode.com/problems/assign-cookies/
"""
from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1
        return i


if __name__ == '__main__':
    assert Solution().findContentChildren([1, 2, 3], [1, 1]) == 1
    assert Solution().findContentChildren([1, 2], [1, 2, 3]) == 2
    assert Solution().findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]) == 2

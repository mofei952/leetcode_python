"""
question:
https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""
from collections import defaultdict
from typing import List


class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_len = len(p)
        s_len = len(s)

        p_counts = defaultdict(int)
        for c in p:
            p_counts[c] += 1

        s_counts = defaultdict(int)
        for c in s[:p_len - 1]:
            s_counts[c] += 1

        res = []
        for i in range(p_len - 1, s_len):
            c = s[i]
            s_counts[c] += 1
            if s_counts == p_counts:
                res.append(i - p_len + 1)
            remove_index = s[i - p_len + 1]
            if s_counts[remove_index] == 1:
                s_counts.pop(remove_index)
            else:
                s_counts[remove_index] -= 1

        print(res)
        return res

    def findAnagrams2(self, s: str, p: str) -> List[int]:
        p_len = len(p)
        s_len = len(s)

        if s_len < p_len:
            return []

        p_counts = defaultdict(int)
        s_counts = defaultdict(int)
        for i in range(p_len):
            p_counts[p[i]] += 1
            s_counts[s[i]] += 1

        res = []
        if s_counts == p_counts:
            res.append(0)
        for i in range(0, s_len - p_len):
            s_counts[s[i + p_len]] += 1
            if s_counts[s[i]] == 1:
                s_counts.pop(s[i])
            else:
                s_counts[s[i]] -= 1
            if s_counts == p_counts:
                res.append(i + 1)

        print(res)
        return res


if __name__ == '__main__':
    assert Solution().findAnagrams2('cbaebabacd', 'abc') == [0, 6]
    assert Solution().findAnagrams2('abab', 'ab') == [0, 1, 2]

from collections import Counter, defaultdict

"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map = defaultdict(int)
        for x in t:
            t_map[x] += 1

        s_map = defaultdict(int)
        i, j = 0, -1
        min_length, min_window = float('inf'), ''
        while j < len(s):
            if all(s_map[k] >= c for k, c in t_map.items()):
                if j-i+1 < min_length:
                    min_length = j-i+1
                    min_window = s[i: j+1]
                i += 1
                if s[i-1] in t_map:
                    s_map[s[i-1]] -= 1
            else:
                j += 1
                if j == len(s):
                    break
                if s[j] in t_map:
                    s_map[s[j]] += 1
        return min_window

    def minWindow2(self, s: str, t: str) -> str:
        need = defaultdict(int)
        for x in t:
            need[x] += 1
        missing = len(t)
        i, left, right = 0, 0, len(s)
        for j in range(len(s)):
            missing -= need[s[j]] > 0
            need[s[j]] -= 1
            if missing == 0:
                while need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if j - i < right - left:
                    left, right = i, j
        return '' if right == len(s) else s[left: right+1]


if __name__ == "__main__":
    print(Solution().minWindow2("ADOBECODEBANC", "ABC"))
    print(Solution().minWindow2("aa", "aa"))
    print(Solution().minWindow2("a", "aa"))

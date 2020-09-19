from collections import defaultdict

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
        

 
if __name__ == "__main__":
    print(Solution().minWindow("ADOBECODEBANC", "ABC"))
    print(Solution().minWindow("aa", "aa"))

"""
Given two strings s and t, return the number of distinct subsequences of s which equals t.
A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters
without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).
It is guaranteed the answer fits on a 32-bit signed integer.

Example 1:
Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit

Example 2:
Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag
 
Constraints:
1 <= s.length, t.length <= 1000
s and t consist of English letters.
"""


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [[1] * len(s) for _ in range(len(t))]
        for i in range(len(t)):
            same = i and t[i] == t[i-1]
            dp[i][0] = 0 if same else (dp[i-1][0] if t[i] == s[0] else 0)
            for j in range(1, len(s)):
                dp[i][j] = dp[i][j-1] + dp[i-1][j-same] if t[i] == s[j] else dp[i][j-1]
            # for line in dp:
            #     print(line)
            # print()
        return dp[-1][-1]
    
    
    def numDistinct2(self, s: str, t: str) -> int:
        dp = [1] + [0] * len(t)
        for i in range(1, len(s)+1):
            prev = 1
            for j in range(1, len(t)+1):
                temp = dp[j]
                if s[i-1] == t[j-1]:
                    dp[j] += prev
                prev = temp
            # for line in dp:
            #     print(line)
            # print()
        return dp[-1]

if __name__ == '__main__':
    print(Solution().numDistinct2('rabbbit', 'rabbit'))
    print(Solution().numDistinct2('rabbbit', 'rabbbit'))
    print(Solution().numDistinct2('babgbag', 'bag'))
    print(Solution().numDistinct2('ddd', 'dd'))
    print(Solution().numDistinct2('aabb', 'abb'))
    print(Solution().numDistinct2('aacaacca', 'ca'))

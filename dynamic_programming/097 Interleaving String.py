"""
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.


Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

Example 3:
Input: s1 = "", s2 = "", s3 = ""
Output: true
 

Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, k = len(s1), len(s2), len(s3)
        if m + n != k:
            return False
        
        dp = [True] * (n+1)
        for j in range(1, n+1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
        for i in range(1, m+1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, n+1):
                dp[j] = (
                    dp[j] and s1[i-1] == s3[i+j-1]
                    or dp[j-1] and s2[j-1] == s3[i+j-1]
                )

        return dp[-1]
    

if __name__ == '__main__':
    print(Solution().isInterleave('aabcc', 'dbbca', 'aadbbcbcac'))
    print(Solution().isInterleave('aabcc', 'dbbca', 'aadbbbaccc'))
    print(Solution().isInterleave('', '', ''))
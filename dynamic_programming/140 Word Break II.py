"""
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences in any order.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:
Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:
Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

Constraints:
1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)

        dp = {0: ['']}
        for i in range(1, len(s)+1):
            cur = []
            for j in dp:
                if s[j:i] in words:
                    if j:
                        cur.extend(t+' '+s[j:i] for t in dp[j])
                    else:
                        cur.append(s[j:i])
            if cur:
                dp[i] = cur

        return dp.get(len(s), [])

    def wordBreak2(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)

        def dfs(idx, res, path):
            if idx == len(s):
                res.append(path.strip())
            for i in range(idx, len(s)):
                if s[idx: i+1] in words:
                    dfs(i+1, res, path + ' ' + s[idx: i+1])

        res = []
        dfs(0, res, '')
        return res

    def wordBreak3(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        dp = [['']]
        for i in range(1, len(s)+1):
            cur = []
            for j in range(len(dp)):
                if dp[j] and s[j:i] in words:
                    if j:
                        cur.extend(t+' '+s[j:i] for t in dp[j])
                    else:
                        cur.append(s[j:i])
            dp.append(cur)
        return dp[-1]


if __name__ == '__main__':
    print(Solution().wordBreak(
        "catsanddog", ["cat", "cats", "and", "sand", "dog"]
    ))
    print(Solution().wordBreak(
        "pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]
    ))
    print(Solution().wordBreak(
        "catsandog", ["cats", "dog", "sand", "and", "cat"]
    ))
    print(Solution().wordBreak(
        '', []
    ))
    print(Solution().wordBreak(
        's', []
    ))
    print(Solution().wordBreak(
        '', ['aa']
    ))

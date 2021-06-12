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
        if not words:
            return []

        dp = {0: ['']}
        for i in range(len(s)):
            cur = []
            for j in dp:
                if s[j:i+1] in words:
                    cur.extend((t and t+' ')+s[j:i+1] for t in dp[j])
            if cur:
                dp[i+1] = cur

        return dp.get(len(s), [])

    def wordBreak2(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)

        def dfs(idx):
            if idx == len(s):
                return ['']
            res = []
            for i in range(idx, len(s)):
                if s[idx: i+1] not in words:
                    continue
                w = s[idx: i+1]
                for t in dfs(i+1):
                    res.append(w + ' ' + t if t else w)
            return res
        
        return dfs(0)


if __name__ == '__main__':
    print(Solution().wordBreak2(
        "catsanddog", ["cat", "cats", "and", "sand", "dog"]
    ))
    print(Solution().wordBreak2(
        "pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]
    ))
    print(Solution().wordBreak2(
        "catsandog", ["cats", "dog", "sand", "and", "cat"]
    ))
    print(Solution().wordBreak2(
        '', []
    ))
    print(Solution().wordBreak2(
        's', []
    ))
    print(Solution().wordBreak2(
        '', ['aa']
    ))

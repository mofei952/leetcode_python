"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true 
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        slen = len(s)
        dp = [False] * (slen+1)
        dp[0] = True
        for i in range(1, slen+1):
            for w in wordDict:
                wlen = len(w)
                if i >= wlen and dp[i-wlen] and s[i-wlen:i] == w:
                    dp[i] = True
                    break
        return dp[-1]

    def wordBreak2(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        max_length = max((len(w) for w in words), default=0)
        dp = [True]
        for i in range(1, len(s)+1):
            dp.append(any(dp[j] and s[j:i] in words for j in range(max(i-max_length, 0), i)))
        return dp[-1]


if __name__ == "__main__":
    print(Solution().wordBreak2('leetcode', ["leet", "code"]))
    print(Solution().wordBreak2('applepenapple', ["apple", "pen"]))
    print(Solution().wordBreak2('catsandog', [
          "cats", "dog", "sand", "and", "cat"]))
    print(Solution().wordBreak2('a', []))
    print(Solution().wordBreak2("dogs", ["dog", "s", "gs"]))
    print(Solution().wordBreak2("ccaccc", ["cc", "ac"]))
    print(Solution().wordBreak2("acccbccb", ["cc", "bc", "ac", "ca"]))

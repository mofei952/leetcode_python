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
        dp = [True]
        for i in range(1, len(s)+1):
            for j in range(len(wordDict)):
                w = wordDict[j]
                wlen = len(w)
                if i >= wlen and s[i-wlen:i] == w and dp[i-wlen]:
                    dp.append(True)
                    break
            else:
                dp.append(False)
        return dp[-1] 


if __name__ == "__main__":
    print(Solution().wordBreak('leetcode', ["leet", "code"]))
    print(Solution().wordBreak('applepenapple', ["apple", "pen"]))
    print(Solution().wordBreak('catsandog', [
          "cats", "dog", "sand", "and", "cat"]))
    print(Solution().wordBreak('a', []))
    print(Solution().wordBreak("dogs", ["dog", "s", "gs"]))
    print(Solution().wordBreak("ccaccc", ["cc", "ac"]))
    print(Solution().wordBreak("acccbccb", ["cc","bc","ac","ca"]))

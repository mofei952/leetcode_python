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
        if not wordDict:
            return False

        dp = [[0] * len(s) for i in range(len(wordDict))]
        for i in range(len(wordDict)):
            w = wordDict[i]
            length = len(w)
            for j in range(len(s)):
                nums = [dp[i][j-1], dp[i-1][j]]
                if w == s[j+1-length:j+1]:
                    wlen = length 
                else:
                    wlen = dp[i-1][j]-dp[i-1][j-1] if j else 0
                # nums.append(dp[i][j-wlen]+wlen)
                if j >= wlen:
                    nums.append(dp[i][j-wlen]+wlen)
                else:
                    nums.append(wlen)
                dp[i][j] = max(nums)

        for row in dp:
            print(row)
        return dp[-1][-1] == len(s)


if __name__ == "__main__":
    print(Solution().wordBreak('leetcode', ["leet", "code"]))
    print(Solution().wordBreak('applepenapple', ["apple", "pen"]))
    print(Solution().wordBreak('catsandog', [
          "cats", "dog", "sand", "and", "cat"]))
    print(Solution().wordBreak('a', []))
    print(Solution().wordBreak("dogs", ["dog", "s", "gs"]))
    print(Solution().wordBreak("ccaccc", ["cc", "ac"]))

"""
question:
https://leetcode.com/problems/longest-palindrome/
"""
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        unpaired_letters = set()
        longest = 0
        for c in s:
            if c in unpaired_letters:
                unpaired_letters.remove(c)
                longest += 2
            else:
                unpaired_letters.add(c)
        if unpaired_letters:
            longest += 1
        return longest

    def longestPalindrome2(self, s: str) -> int:
        letter_counts = Counter(s)
        odd_count = sum(c % 2 for c in letter_counts.values())
        return len(s) if odd_count == 0 else len(s) - odd_count + 1


if __name__ == '__main__':
    assert Solution().longestPalindrome2('abccccdd') == 7
    assert Solution().longestPalindrome2('a') == 1
    assert Solution().longestPalindrome2('bb') == 2
    assert Solution().longestPalindrome2('') == 0

"""
question:
https://leetcode.com/problems/remove-duplicate-letters/
"""
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        counter = Counter(s)
        for c in s:
            if c not in stack:
                while stack and stack[-1] > c and counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            counter[c] -= 1
        return ''.join(stack)


if __name__ == '__main__':
    assert Solution().removeDuplicateLetters('bcabc') == 'abc'
    assert Solution().removeDuplicateLetters('cbacdcbc') == 'acdb'
    assert Solution().removeDuplicateLetters('cbacfcbce') == 'acfbe'
    assert Solution().removeDuplicateLetters('bbcaac') == 'bac'

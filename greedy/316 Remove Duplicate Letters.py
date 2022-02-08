"""
question:
https://leetcode.com/problems/remove-duplicate-letters/
"""
from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        visited = set()
        last_occ = {c: i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            if c in visited:
                continue
            while stack and stack[-1] > c and last_occ[stack[-1]] > i:
                visited.remove(stack.pop())
            stack.append(c)
            visited.add(c)
        return ''.join(stack)


if __name__ == '__main__':
    assert Solution().removeDuplicateLetters('bcabc') == 'abc'
    assert Solution().removeDuplicateLetters('cbacdcbc') == 'acdb'
    assert Solution().removeDuplicateLetters('cbacfcbce') == 'acfbe'
    assert Solution().removeDuplicateLetters('bbcaac') == 'bac'

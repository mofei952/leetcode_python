"""
question:
https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
"""


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        stack = []
        for s in preorder.split(','):
            stack.append(s)
            while len(stack) >= 3 and stack[-1] == stack[-2] == '#' and stack[-3] != '#':
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('#')
        return stack == ['#']

    def isValidSerialization2(self, preorder: str) -> bool:
        count = 1
        for c in preorder.split(','):
            if count == 0:
                return False
            count += 1 if c != '#' else -1
        return count == 0


if __name__ == '__main__':
    assert Solution().isValidSerialization2("9,3,4,#,#,1,#,#,2,#,6,#,#") is True
    assert Solution().isValidSerialization2("1,#") is False
    assert Solution().isValidSerialization2("9,#,#,1") is False
    assert Solution().isValidSerialization2("#") is True

"""
question:
https://leetcode.com/problems/sum-root-to-leaf-numbers/
"""
from functools import reduce
from typing import Optional

from tree.binary_tree import create_tree, TreeNode


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def nums(node):
            if node is None:
                return []
            if node.left is None and node.right is None:
                return [str(node.val)]
            return [str(node.val) + n for n in nums(node.left) + nums(node.right)]

        return sum(int(n) for n in nums(root))

    def sumNumbers2(self, root: Optional[TreeNode]) -> int:
        res = 0
        stack = []
        node = root
        last_visit = None
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack[-1]
            if node.right is None or node.right == last_visit:
                stack.pop()
                if node.left is None and node.right is None:
                    # res += int(''.join([str(n.val) for n in stack + [node]]))
                    # res += sum(val * 10 ** i for i, val in enumerate([n.val for n in stack + [node]][::-1]))
                    res += reduce(lambda a, b: a * 10 + b, [n.val for n in stack + [node]])
                last_visit = node
                node = None
            else:
                node = node.right
        return res

    def sumNumbers3(self, root: Optional[TreeNode]) -> int:
        def recursive(node, num):
            if node is None:
                return 0
            num = num * 10 + node.val
            if node.left is None and node.right is None:
                return num
            return recursive(node.left, num) + recursive(node.right, num)

        return recursive(root, 0)


if __name__ == '__main__':
    assert Solution().sumNumbers3(create_tree([1, 2, 3])) == 25
    assert Solution().sumNumbers3(create_tree([4, 9, 0, 5, 1])) == 1026
    assert Solution().sumNumbers3(create_tree([])) == 0

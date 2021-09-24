"""
question:
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""
from typing import Optional

from tree.binary_tree import TreeNode, create_tree


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if k == 1:
                return node.val
            k -= 1
            node = node.right


if __name__ == '__main__':
    assert Solution().kthSmallest(create_tree([3, 1, 4, None, 2]), 1) == 1
    assert Solution().kthSmallest(create_tree([5, 3, 6, 2, 4, None, None, 1]), 3) == 3

"""
question:
https://leetcode.cn/problems/legal-binary-search-tree-lcci/
"""

from tree.binary_tree import TreeNode, create_tree


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def is_range(node, min_val, max_val):
            if not node:
                return True
            if not min_val <= node.val <= max_val:
                return False
            if not is_range(node.left, min_val, node.val - 1):
                return False
            if not is_range(node.right, node.val + 1, max_val):
                return False
            return True

        return is_range(root, float('-inf'), float('inf'))

    def isValidBST2(self, root: TreeNode) -> bool:
        stack = []
        node = root
        last_val = float('-inf')
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()

            if node.val <= last_val:
                return False
            last_val = node.val

            node = node.right
        return True


if __name__ == '__main__':
    assert Solution().isValidBST2(create_tree([2, 1, 3])) is True
    assert Solution().isValidBST2(create_tree([5, 1, 4, None, None, 3, 6])) is False

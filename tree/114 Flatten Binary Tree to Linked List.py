"""
question:
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""

from tree.binary_tree import TreeNode, create_tree


class Solution:

    def recursive(self, node):
        if not node:
            return
        left, right = node.left, node.right
        if left:
            node.left = None
            node.right = left
            node = self.recursive(left)
        if right:
            node.right = right
            node = self.recursive(right)
        return node

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.recursive(root)

    def flatten2(self, root: TreeNode) -> None:
        if root is None:
            return None
        stack = [root]
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node.right = stack[-1] if stack else None
            node.left = None


if __name__ == '__main__':
    tree = create_tree([1, 2, 5, 3, 4, None, 6])
    Solution().flatten2(tree)
    tree.display()

    tree = create_tree([])
    Solution().flatten2(tree)

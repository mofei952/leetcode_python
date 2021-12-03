"""
question:
https://leetcode.com/problems/recover-binary-search-tree/
"""
from typing import Optional

from tree.binary_tree import TreeNode, create_tree, is_same_tree


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []

        vals = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            vals.append(node.val)
            node = node.right

        vals.sort()
        node = root
        i = 0
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.val = vals[i]
            i += 1
            node = node.right

    first_node = None
    second_node = None
    prev_node = TreeNode(float('-inf'))

    def recoverTree2(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.traverse(root)
        self.first_node.val, self.second_node.val = self.second_node.val, self.first_node.val

    def traverse(self, root):
        if root is None:
            return

        self.traverse(root.left)

        if self.first_node is None and self.prev_node.val >= root.val:
            self.first_node = self.prev_node
        if self.first_node and self.prev_node.val >= root.val:
            self.second_node = root
        self.prev_node = root

        self.traverse(root.right)


if __name__ == '__main__':
    t1 = create_tree([1, 3, None, None, 2])
    t2 = create_tree([3, 1, None, None, 2])
    Solution().recoverTree2(t1)
    assert is_same_tree(t1, t2)

    t1 = create_tree([3, 1, 4, None, None, 2])
    t2 = create_tree([2, 1, 4, None, None, 3])
    Solution().recoverTree2(t1)
    assert is_same_tree(t1, t2)

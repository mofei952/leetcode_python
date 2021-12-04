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

    def recoverTree2(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        first = None
        second = None
        prev = TreeNode(float('-inf'))

        def traversal(curr):
            nonlocal first, second, prev

            if curr is None:
                return
            traversal(curr.left)

            if first is None and prev.val >= curr.val:
                first = prev
            if first and prev.val >= curr.val:
                second = curr
            prev = curr

            traversal(curr.right)

        traversal(root)
        first.val, second.val = second.val, first.val

    def recoverTree3(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev, curr = TreeNode(float('-inf')), root
        first = second = None
        stack = []

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()

            if prev.val > curr.val:
                if first is None:
                    first = prev
                second = curr
            prev = curr

            curr = curr.right

        first.val, second.val = second.val, first.val


if __name__ == '__main__':
    t1 = create_tree([1, 3, None, None, 2])
    t2 = create_tree([3, 1, None, None, 2])
    Solution().recoverTree2(t1)
    assert is_same_tree(t1, t2)

    t1 = create_tree([3, 1, 4, None, None, 2])
    t2 = create_tree([2, 1, 4, None, None, 3])
    Solution().recoverTree2(t1)
    assert is_same_tree(t1, t2)

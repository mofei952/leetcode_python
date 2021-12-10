"""
question:
https://leetcode.com/problems/validate-binary-search-tree/
"""
from typing import Optional

from tree.binary_tree import create_tree, TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """ 递归先序遍历解法 """

        def validate(node, low, high):
            if node is None:
                return True
            if not low < node.val < high:
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root, float('-inf'), float('inf'))

    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        """ 递归中序遍历解法 """
        prev = float('-inf')

        def inorder(node):
            nonlocal prev
            if node is None:
                return True

            if inorder(node.left) is False:
                return False

            if prev and node.val <= prev:
                return False
            prev = node.val

            if inorder(node.right) is False:
                return False
            return True

        return inorder(root)

    def isValidBST3(self, root: Optional[TreeNode]) -> bool:
        """ 非递归中序遍历解法（非递归的效率更高） """
        stack = []
        node = root
        prev = float('-inf')

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()

            if node.val <= prev:
                return False
            prev = node.val

            node = node.right

        return True


if __name__ == '__main__':
    assert Solution().isValidBST3(create_tree([2, 1, 3])) is True
    assert Solution().isValidBST3(create_tree([5, 1, 4, None, None, 3, 6])) is False
    assert Solution().isValidBST3(create_tree([5, 1, 7, None, None, 4, 8])) is False
    assert Solution().isValidBST3(create_tree([])) is True
    assert Solution().isValidBST3(create_tree([2, 2, 2])) is False

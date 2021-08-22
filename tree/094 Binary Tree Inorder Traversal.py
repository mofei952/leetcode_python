"""
question:
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""

from typing import Optional
from typing import List

from tree.binary_tree import TreeNode


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        res = []
        inorder(root)
        return res

    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res


if __name__ == '__main__':
    print(Solution().inorderTraversal2(
        TreeNode.create_tree([])
    ))
    print(Solution().inorderTraversal2(
        TreeNode.create_tree([1])
    ))
    print(Solution().inorderTraversal2(
        TreeNode.create_tree([1, None, 2, 3])
    ))

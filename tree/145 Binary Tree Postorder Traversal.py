"""
quesiont:
https://leetcode.com/problems/binary-tree-postorder-traversal/
"""
from typing import Optional, List

from tree.binary_tree import TreeNode, create_tree


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(node):
            if node is None:
                return
            postorder(node.left)
            postorder(node.right)
            res.append(node.val)

        res = []
        postorder(root)
        return res


if __name__ == '__main__':
    assert Solution().postorderTraversal2(create_tree([1, None, 2, 3])) == [3, 2, 1]
    assert Solution().postorderTraversal2(create_tree([])) == []
    assert Solution().postorderTraversal2(create_tree([1])) == [1]

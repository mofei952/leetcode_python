"""
question:
https://leetcode.com/problems/invert-binary-tree/
"""
from typing import Optional

from tree.binary_tree import create_tree, TreeNode, is_same_tree


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


if __name__ == '__main__':
    func = Solution().invertTree

    t1 = create_tree([4, 2, 7, 1, 3, 6, 9])
    t2 = create_tree([4, 7, 2, 9, 6, 3, 1])
    assert is_same_tree(func(t1), t2)

    t1 = create_tree([2, 1, 3])
    t2 = create_tree([2, 3, 1])
    assert is_same_tree(func(t1), t2)

    t1 = create_tree([])
    t2 = create_tree([])
    assert is_same_tree(func(t1), t2)

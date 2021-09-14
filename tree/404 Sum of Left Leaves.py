"""
question:
https://leetcode.com/problems/sum-of-left-leaves/
"""
from typing import Optional

from tree.binary_tree import create_tree, TreeNode


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        res = 0
        if root.left:
            left_node = root.left
            if left_node.left is None and left_node.right is None:
                res += left_node.val
            else:
                res += self.sumOfLeftLeaves(left_node)
        if root.right:
            res += self.sumOfLeftLeaves(root.right)
        return res

    def sumOfLeftLeaves2(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def add_left_leaves(node):
            if node.left:
                left_node = node.left
                if left_node.left is None and left_node.right is None:
                    self.res += left_node.val
                else:
                    add_left_leaves(left_node)
            if node.right:
                add_left_leaves(node.right)

        self.res = 0
        add_left_leaves(root)
        return self.res


if __name__ == '__main__':
    assert Solution().sumOfLeftLeaves2(create_tree([3, 9, 20, None, None, 15, 7])) == 24
    assert Solution().sumOfLeftLeaves2(create_tree([1])) == 0

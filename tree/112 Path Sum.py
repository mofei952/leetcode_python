"""
question:
https://leetcode.com/problems/path-sum/
"""

from tree.binary_tree import TreeNode, create_tree


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False

        def _hasPathSum(node, target):
            if not node.left and not node.right:
                return node.val == target
            if node.left and self.hasPathSum(node.left, target - node.val):
                return True
            if node.right and self.hasPathSum(node.right, target - node.val):
                return True
            return False

        return _hasPathSum(root, targetSum)


if __name__ == '__main__':
    assert Solution().hasPathSum(create_tree([]), 0) is False
    assert Solution().hasPathSum(create_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22) is True
    assert Solution().hasPathSum(create_tree([1, 2]), 1) is False

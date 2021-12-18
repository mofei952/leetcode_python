"""
question:
https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""
from typing import Optional

from tree.binary_tree import TreeNode, create_tree


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = float('-inf')

        def dfs(node):
            nonlocal result
            if node is None:
                return 0
            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            result = max(result, node.val + left_max + right_max)
            return node.val + max(left_max, right_max)

        dfs(root)
        return result


if __name__ == '__main__':
    assert Solution().maxPathSum(create_tree([1, 2, 3])) == 6
    assert Solution().maxPathSum(create_tree([-10, 9, 20, None, None, 15, 7])) == 42
    assert Solution().maxPathSum(create_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1])) == 48

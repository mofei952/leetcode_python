"""
question:
https://leetcode.com/problems/house-robber-iii/
"""

from tree.binary_tree import TreeNode, create_tree


class Solution:
    def rob(self, root: TreeNode) -> int:
        def recursive(node):
            if node is None:
                return 0, 0
            lrob, lnotrob = recursive(node.left)
            rrob, rnotlab = recursive(node.right)
            return node.val + lnotrob + rnotlab, max(lrob, lnotrob) + max(rrob, rnotlab)

        return max(recursive(root))


if __name__ == '__main__':
    print(Solution().rob(create_tree([3, 2, 3, None, 3, None, 1])))
    print(Solution().rob(create_tree([3, 4, 5, 1, 3, None, 1])))

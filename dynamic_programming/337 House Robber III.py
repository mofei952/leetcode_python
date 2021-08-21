"""
The thief has found himself a new place for his thievery again.
There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that all houses in this place form a binary tree.
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.
"""

from tree.binary_tree import TreeNode, create_tree


class Solution:
    def rob(self, root: TreeNode) -> int:
        def traverse(node):
            if node is None:
                return 0, 0
            lrob, lnotrob = traverse(node.left)
            rrob, rnotlab = traverse(node.right)
            return node.val+lnotrob+rnotlab, max(lrob, lnotrob)+max(rrob, rnotlab)
        return max(traverse(root))


if __name__ == '__main__':
    print(Solution().rob(create_tree([3, 2, 3, None, 3, None, 1])))
    print(Solution().rob(create_tree([3, 4, 5, 1, 3, None, 1])))

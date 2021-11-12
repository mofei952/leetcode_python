"""
question:
https://leetcode.com/problems/path-sum-iii/
"""
from typing import Optional

from tree.binary_tree import TreeNode, create_tree


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def pathCount(root, sums):
            if root is None:
                return 0

            sums = [sum + root.val for sum in sums]
            sums.append(root.val)
            count = sums.count(targetSum)

            lcount = pathCount(root.left, sums)
            rcount = pathCount(root.right, sums)

            return count + lcount + rcount

        return pathCount(root, [])


if __name__ == '__main__':
    assert Solution().pathSum(create_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]), 8) == 3
    assert Solution().pathSum(create_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], ), 22) == 3
    assert Solution().pathSum(create_tree([1]), 1) == 1
    assert Solution().pathSum(create_tree([]), 0) == 0
    assert Solution().pathSum(create_tree([-2, None, -3]), -5) == 1
    assert Solution().pathSum(create_tree([1, -2, -3, 1, 3, -2, None, -1]), -1) == 4

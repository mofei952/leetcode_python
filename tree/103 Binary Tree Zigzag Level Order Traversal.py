"""
question:
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""
from typing import Optional, List

from tree.binary_tree import TreeNode, create_tree


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = [root]
        res = []
        flag = 0

        while queue:
            flag = flag ^ 1
            res.append([n.val for n in (queue if flag else queue[::-1])])

            new_queue = []
            for node in queue:
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue

        return res


if __name__ == '__main__':
    assert Solution().zigzagLevelOrder(create_tree([3, 9, 20, None, None, 15, 7])) == [[3], [20, 9], [15, 7]]
    assert Solution().zigzagLevelOrder(create_tree([1])) == [[1]]
    assert Solution().zigzagLevelOrder(create_tree([])) == []

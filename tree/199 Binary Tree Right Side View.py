"""
question:
https://leetcode.com/problems/binary-tree-right-side-view/
"""
from typing import Optional, List

from tree.binary_tree import TreeNode, create_tree


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        queue = [root]
        while queue:
            res.append(queue[-1].val)
            next_queue = []
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
        return res


if __name__ == '__main__':
    assert Solution().rightSideView(create_tree([1, 2, 3, None, 5, None, 4])) == [1, 3, 4]
    assert Solution().rightSideView(create_tree([1, None, 3])) == [1, 3]
    assert Solution().rightSideView(create_tree([])) == []
    assert Solution().rightSideView(create_tree([1, 2, 3, 4])) == [1, 3, 4]

"""
question:
https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""

from tree.binary_tree import TreeNode, create_tree


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        def _minDepth(node):
            if not node.left and not node.right:
                return 1
            depths = []
            if node.left:
                depths.append(self.minDepth(node.left))
            if node.right:
                depths.append(self.minDepth(node.right))
            return 1 + min(depths)

        return _minDepth(root)

    def minDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        depth = 1
        while queue:
            new_queue = []
            for node in queue:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            queue = new_queue
            depth += 1


if __name__ == '__main__':
    assert Solution().minDepth(create_tree([1, 2])) == 2
    assert Solution().minDepth(create_tree([1, 2, 3, 4, None, None, 5])) == 3
    assert Solution().minDepth(create_tree([3, 9, 20, None, None, 15, 7])) == 2

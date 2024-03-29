"""
question:
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""
from typing import List

from tree.binary_tree import TreeNode, create_tree


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """二叉树的层序遍历"""
        if not root:
            return []
        queue = [(root, 0)]
        result = []
        while queue:
            node, level = queue.pop(0)
            if level >= len(result):
                result.append([])
            result[-1].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return result

    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        """二叉树的层序遍历 优化"""
        if root is None:
            return []
        queue = [root]
        result = []
        while queue:
            result.append([])
            next_queue = []
            for node in queue:
                result[-1].append(node.val)
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
        return result


if __name__ == '__main__':
    assert Solution().levelOrder2(create_tree([3, 9, 20, None, None, 15, 7])) == [[3], [9, 20], [15, 7]]

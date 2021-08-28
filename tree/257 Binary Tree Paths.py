"""
question:
https://leetcode.com/problems/binary-tree-paths/
"""
from typing import Optional, List

from tree.binary_tree import TreeNode, create_tree


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return ['']

        def find(node, path):
            if not node.left and not node.right:
                res.append(path)
                return
            if node.left:
                find(node.left, f'{path}->{node.left.val}')
            if node.right:
                find(node.right, f'{path}->{node.right.val}')

        res = []
        find(root, str(root.val))
        return res

    def binaryTreePaths2(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return ['']

        queue = [(root, str(root.val))]
        paths = []
        while queue:
            node, path = queue.pop(0)
            if not node.left and not node.right:
                paths.append(path)
                continue
            if node.left:
                queue.append((node.left, f'{path}->{node.left.val}'))
            if node.right:
                queue.append((node.right, f'{path}->{node.right.val}'))

        return paths


if __name__ == '__main__':
    assert set(Solution().binaryTreePaths2(create_tree([1, 2, 3, None, 5]))) == {'1->2->5', '1->3'}
    assert Solution().binaryTreePaths2(create_tree([1])) == ['1']
    assert Solution().binaryTreePaths2(create_tree([])) == ['']

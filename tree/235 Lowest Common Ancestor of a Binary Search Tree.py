"""
question:
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
"""
from tree.binary_tree import TreeNode, create_tree


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        node = root
        while root:
            if p.val == node.val or q.val == node.val:
                return node
            if p.val < node.val < q.val:
                return node
            if q.val < node.val:
                node = node.left
            elif p.val > node.val:
                node = node.right

    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        node = root
        while root:
            if q.val < node.val:
                node = node.left
            elif p.val > node.val:
                node = node.right
            else:
                return node


if __name__ == '__main__':
    root = create_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    assert Solution().lowestCommonAncestor2(root, root.left, root.right) == root

    root = create_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    assert Solution().lowestCommonAncestor2(root, root.left, root.left.right) == root.left

    root = create_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    assert Solution().lowestCommonAncestor2(root, root.right, root.right.left) == root.right

    root = create_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    assert Solution().lowestCommonAncestor2(root, root.left.right.right, root.right) == root

    root = create_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
    assert Solution().lowestCommonAncestor2(root, root.left, root.left) == root.left

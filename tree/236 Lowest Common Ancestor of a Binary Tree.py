"""
question:
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""
from tree.binary_tree import TreeNode, create_tree


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node_to_parent = {}
        queue = [root]
        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
                node_to_parent[node.left.val] = node
            if node.right:
                queue.append(node.right)
                node_to_parent[node.right.val] = node

        pnode_parents = []
        while p:
            pnode_parents.append(p)
            p = node_to_parent.get(p.val)

        while q:
            if q in pnode_parents:
                return q
            q = node_to_parent.get(q.val)


if __name__ == '__main__':
    root = create_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    assert Solution().lowestCommonAncestor(root, root.left, root.right) == root

    root = create_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
    assert Solution().lowestCommonAncestor(root, root.left, root.left.right.right) == root.left

    root = create_tree([1, 2])
    assert Solution().lowestCommonAncestor(root, root, root.left) == root

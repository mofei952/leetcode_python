"""
question:
https://leetcode.com/problems/same-tree/
"""

from tree.binary_tree import TreeNode, create_tree


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        queue = [(p, q)]
        while queue:
            n1, n2 = queue.pop(0)
            if not n1 and not n2:
                continue
            if not n1 or not n2:
                return False
            if n1.val != n2.val:
                return False
            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))
        return True


if __name__ == '__main__':
    assert Solution().isSameTree2(create_tree([1, 2, 3]), create_tree([1, 2, 3])) is True
    assert Solution().isSameTree2(create_tree([1, 2, 1]), create_tree([1, 1, 2])) is False

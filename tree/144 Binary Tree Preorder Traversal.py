"""
question:
https://leetcode.com/problems/binary-tree-preorder-traversal/
"""
from typing import Optional, List

from tree.binary_tree import TreeNode, create_tree


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    def preorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(node):
            if node is None:
                return
            res.append(node.val)
            postorder(node.left)
            postorder(node.right)

        res = []
        postorder(root)
        return res

    def preorderTraversal3(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        node = root
        while node or stack:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res

    def preorderTraversal4(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res

    def preorderTraversal5(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        res = []
        while cur:
            right_most = cur.left
            if right_most is None:
                res.append(cur.val)
                cur = cur.right
                continue
            while right_most.right and right_most.right != cur:
                right_most = right_most.right
            if right_most.right is None:
                res.append(cur.val)
                right_most.right = cur
                cur = cur.left
            else:
                right_most.right = None
                cur = cur.right
        return res


if __name__ == '__main__':
    assert Solution().preorderTraversal5(create_tree([1, None, 2, 3])) == [1, 2, 3]
    assert Solution().preorderTraversal5(create_tree([])) == []
    assert Solution().preorderTraversal5(create_tree([1])) == [1]

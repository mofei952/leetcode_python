"""
question:
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""

from typing import Optional
from typing import List

from tree.binary_tree import TreeNode, create_tree


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            res.append(node.val)
            inorder(node.right)

        res = []
        inorder(root)
        return res

    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
        return res

    def inorderTraversal3(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        stack = [(root, 0)]
        while stack:
            node, flag = stack.pop()
            if flag == 0:
                if node.right:
                    stack.append((node.right, 0))
                stack.append((node, 1))
                if node.left:
                    stack.append((node.left, 0))
            else:
                res.append(node.val)
        return res

    def inorderTraversal4(self, root: Optional[TreeNode]) -> List[int]:
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
                right_most.right = cur
                cur = cur.left
            else:
                right_most.right = None
                res.append(cur.val)
                cur = cur.right
        return res


if __name__ == '__main__':
    assert Solution().inorderTraversal4(create_tree([])) == []
    assert Solution().inorderTraversal4(create_tree([1])) == [1]
    assert Solution().inorderTraversal4(create_tree([1, None, 2, 3])) == [1, 3, 2]

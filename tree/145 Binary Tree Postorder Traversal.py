"""
question:
https://leetcode.com/problems/binary-tree-postorder-traversal/
"""
from typing import Optional, List

from tree.binary_tree import TreeNode, create_tree


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    def postorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(node):
            if node is None:
                return
            postorder(node.left)
            postorder(node.right)
            res.append(node.val)

        res = []
        postorder(root)
        return res

    def postorderTraversal3(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        node = root
        last_visited = None
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack[-1]
            if node.right is None or node.right == last_visited:
                stack.pop()
                res.append(node.val)
                last_visited = node
                node = None
            else:
                node = node.right
        return res

    def postorderTraversal4(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        return res[::-1]


if __name__ == '__main__':
    assert Solution().postorderTraversal4(create_tree([1, None, 2, 3])) == [3, 2, 1]
    assert Solution().postorderTraversal4(create_tree([])) == []
    assert Solution().postorderTraversal4(create_tree([1])) == [1]

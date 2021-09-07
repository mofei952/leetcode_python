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
        last_visit = None
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack[-1]
            if node.right is None or node.right == last_visit:
                stack.pop()
                res.append(node.val)
                last_visit = node
                node = None
            else:
                node = node.right
        return res

    def postorderTraversal4(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        node = root
        while node or stack:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.right
            node = stack.pop()
            node = node.left
        return res[::-1]

    def postorderTraversal5(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        stack = [(root, 0)]
        while stack:
            node, flag = stack.pop()
            if flag == 0:
                stack.append((node, 1))
                if node.right:
                    stack.append((node.right, 0))
                if node.left:
                    stack.append((node.left, 0))
            else:
                res.append(node.val)
        return res

    def postorderTraversal6(self, root: Optional[TreeNode]) -> List[int]:
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

    def postorderTraversal7(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        res = []
        while cur:
            left_most = cur.right
            if left_most is None:
                res.append(cur.val)
                cur = cur.left
                continue
            while left_most.left and left_most.left != cur:
                left_most = left_most.left
            if left_most.left is None:
                res.append(cur.val)
                left_most.left = cur
                cur = cur.right
            else:
                left_most.left = None
                cur = cur.left
        return res[::-1]


if __name__ == '__main__':
    assert Solution().postorderTraversal7(create_tree([1, None, 2, 3])) == [3, 2, 1]
    assert Solution().postorderTraversal7(create_tree([])) == []
    assert Solution().postorderTraversal7(create_tree([1])) == [1]

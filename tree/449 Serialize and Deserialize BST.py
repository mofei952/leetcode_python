"""
question:
https://leetcode.com/problems/serialize-and-deserialize-bst/
"""
from tree.binary_tree import create_tree, TreeNode


class Codec:
    def preorder(self, root):
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

    def inorder(self, root):
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

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        return str((self.preorder(root), self.inorder(root)))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        preorder, inorder = eval(data)
        if not preorder or not inorder:
            return None

        inorder_indexes = {v: i for i, v in enumerate(inorder)}

        def recursive(left, right):
            if left > right:
                return None

            val = preorder.pop(0)
            node = TreeNode(val)

            node.left = recursive(left, inorder_indexes[val] - 1)
            node.right = recursive(inorder_indexes[val] + 1, right)

            return node

        tree = recursive(0, len(inorder) - 1)
        return tree


if __name__ == '__main__':
    root = create_tree([2, 1, 3])
    ser = Codec()
    deser = Codec()
    tree = ser.serialize(root)
    ans = deser.deserialize(tree)
    ans.display()

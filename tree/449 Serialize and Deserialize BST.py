"""
question:
https://leetcode.com/problems/serialize-and-deserialize-bst/
"""
from tree.binary_tree import create_tree, TreeNode


class Codec:
    def preorder_traversal(self, root):
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

    def inorder_traversal(self, root):
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
        return str((self.preorder_traversal(root), self.inorder_traversal(root)))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        preorder, inorder = eval(data)
        preorder_index = 0
        inorder_indexes = {v: i for i, v in enumerate(inorder)}

        def recursive(left, right):
            nonlocal preorder_index
            if left == right:
                return None

            val = preorder[preorder_index]
            preorder_index += 1
            node = TreeNode(val)

            node.left = recursive(left, inorder_indexes[val])
            node.right = recursive(inorder_indexes[val] + 1, right)

            return node

        tree = recursive(0, len(inorder))
        return tree


if __name__ == '__main__':
    root = create_tree([2, 1, 3])
    ser = Codec()
    deser = Codec()
    tree = ser.serialize(root)
    ans = deser.deserialize(tree)
    ans.display()

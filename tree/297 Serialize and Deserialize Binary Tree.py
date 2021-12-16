"""
question:
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
"""
import json

from tree.binary_tree import create_tree, TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []

        queue = [root]
        while queue:
            node = queue.pop(0)
            if node is None:
                result.append(None)
                continue
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)

        while result and result[-1] is None:
            result.pop()

        return json.dumps(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        arr = json.loads(data)
        if not arr:
            return None

        length = len(arr)
        root = TreeNode(arr[0])
        queue = [root]
        for i in range(1, length, 2):
            node = queue.pop(0)

            if arr[i] is not None:
                node.left = TreeNode(arr[i])
                queue.append(node.left)

            if i + 1 >= length:
                continue
            if arr[i + 1] is not None:
                node.right = TreeNode(arr[i + 1])
                queue.append(node.right)

        return root


if __name__ == '__main__':
    ser = Codec()

    tree = create_tree([1, 2, 3, None, None, 4, 5])
    ans = ser.deserialize(ser.serialize(tree))
    assert tree == ans

    tree = create_tree([])
    ans = ser.deserialize(ser.serialize(tree))
    assert tree == ans

    tree = create_tree([1])
    ans = ser.deserialize(ser.serialize(tree))
    assert tree == ans

    tree = create_tree([1, 2])
    ans = ser.deserialize(ser.serialize(tree))
    assert tree == ans

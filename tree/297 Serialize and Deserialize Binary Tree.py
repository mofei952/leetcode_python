"""
question:
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
"""
from collections import deque

from tree.binary_tree import create_tree, TreeNode


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []

        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node is None:
                result.append('N')
                continue
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        return ','.join(result).rstrip(',N')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        arr = data.split(',')
        length = len(arr)

        root = TreeNode(arr[0])
        queue = deque()
        queue.append(root)

        for i in range(1, length, 2):
            node = queue.popleft()

            if arr[i] != 'N':
                node.left = TreeNode(int(arr[i]))
                queue.append(node.left)

            if i + 1 >= length:
                continue
            if arr[i + 1] != 'N':
                node.right = TreeNode(int(arr[i + 1]))
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

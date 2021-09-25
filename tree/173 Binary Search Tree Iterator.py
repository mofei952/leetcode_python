"""
question:
https://leetcode.com/problems/binary-search-tree-iterator/
"""
from typing import Optional

from tree.binary_tree import TreeNode, create_tree


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.node = root

    def next(self) -> int:
        while self.node or self.stack:
            while self.node:
                self.stack.append(self.node)
                self.node = self.node.left
            self.node = self.stack.pop()
            res = self.node.val
            self.node = self.node.right
            return res

    def hasNext(self) -> bool:
        return bool(self.node or self.stack)


class BSTIterator2:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        cur_node = self.stack.pop()

        node = cur_node.right
        while node:
            self.stack.append(node)
            node = node.left

        return cur_node.val

    def hasNext(self) -> bool:
        return bool(self.stack)


if __name__ == '__main__':
    iterator = BSTIterator2(create_tree([7, 3, 15, None, None, 9, 20]))
    assert iterator.next() == 3
    assert iterator.next() == 7
    assert iterator.hasNext() is True
    assert iterator.next() == 9
    assert iterator.hasNext() is True
    assert iterator.next() == 15
    assert iterator.hasNext() is True
    assert iterator.next() == 20
    assert iterator.hasNext() is False

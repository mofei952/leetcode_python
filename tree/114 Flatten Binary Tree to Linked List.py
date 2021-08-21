#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/22 15:47
# @File    : 114 Flatten Binary Tree to Linked List.py
# @Software: PyCharm

"""
Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:
    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:
1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""

from tree.binary_tree import TreeNode, create_tree


class Solution:

    def recursive(self, node):
        if not node:
            return
        left, right = node.left, node.right
        if left:
            node.left = None
            node.right = left
            node = self.recursive(left)
        if right:
            node.right = right
            node = self.recursive(right)
        return node

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.recursive(root)


if __name__ == '__main__':
    tree = create_tree([1, 2, 5, 3, 4, None, 6])
    Solution().flatten(tree)
    print(tree)

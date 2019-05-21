#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/20 19:15
# @File    : 111 Minimum Depth of Binary Tree.py
# @Software: PyCharm

"""
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""

from tree.tree_node import TreeNode


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        depths = []
        if root.left:
            depths.append(self.minDepth(root.left))
        if root.right:
            depths.append(self.minDepth(root.right))
        return 1 + min(depths)


if __name__ == '__main__':
    print(Solution().minDepth(TreeNode.create_tree([1, 2])))
    print(Solution().minDepth(TreeNode.create_tree([1, 2, 3, 4, None, None, 5])))
    print(Solution().minDepth(TreeNode.create_tree([3, 9, 20, None, None, 15, 7])))

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/21 19:21
# @File    : 112 Path Sum.py
# @Software: PyCharm

"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""

from tree.binary_tree import TreeNode


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum
        if root.left and self.hasPathSum(root.left, sum - root.val):
            return True
        if root.right and self.hasPathSum(root.right, sum - root.val):
            return True
        return False


if __name__ == '__main__':
    print(Solution().hasPathSum(TreeNode.create_tree([]), 0))
    print(Solution().hasPathSum(TreeNode.create_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22))
    print(Solution().hasPathSum(TreeNode.create_tree([1, 2]), 1))

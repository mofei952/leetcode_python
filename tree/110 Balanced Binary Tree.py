#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/18 19:32
# @File    : 110 Balanced Binary Tree.py
# @Software: PyCharm

"""
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:
Given the following tree [3,9,20,None,None,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:
Given the following tree [1,2,2,3,3,None,None,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""

from tree.tree_node import TreeNode


class Solution:
    balance = True

    def isBalanced(self, root):
        def isBalance(node):
            if not node:
                return 0
            h1 = isBalance(node.left)
            h2 = isBalance(node.right)
            if abs(h1 - h2) > 1:
                self.balance = False
            return 1 + max(h1, h2)

        isBalance(root)
        return self.balance


if __name__ == '__main__':
    print(Solution().isBalanced(TreeNode.create_tree([1, None, 2, None, 3])))
    print(Solution().isBalanced(TreeNode.create_tree([3, 9, 20, None, None, 15, 7])))
    print(Solution().isBalanced(TreeNode.create_tree([1, 2, 2, 3, 3, None, None, 4, 4])))

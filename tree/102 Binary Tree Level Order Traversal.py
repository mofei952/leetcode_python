#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/3/14 20:17
# @File    : 102 Binary Tree Level Order Traversal.py
# @Software: PyCharm

"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""
from typing import List

from tree.tree_node import TreeNode


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """二叉树的层序遍历"""
        if not root:
            return []
        stack = [(root, 0)]
        result = []
        while stack:
            node, level = stack.pop(0)
            if level >= len(result):
                result.append([])
            result[-1].append(node.val)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
        return result


if __name__ == '__main__':
    # print(TreeNode.create_tree([3, 9, 20, None, None, 15, 7]))
    result = Solution().levelOrder(TreeNode.create_tree([3, 9, 20, None, None, 15, 7]))
    print(result)

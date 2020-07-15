#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/9 19:04
# @File    : test106.py
# @Software: PyCharm

"""
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
"""

from typing import List

from tree.tree_node import TreeNode


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        val = postorder[-1]
        index = inorder.index(val)
        node = TreeNode(val)
        node.left = self.buildTree(inorder[:index], postorder[:index])
        node.right = self.buildTree(inorder[index + 1:], postorder[index:-1])
        return node

    def buildTree2(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return

        inorder_indexes = {v: i for i, v in enumerate(inorder)}

        def buildTree_recursive(left, right):
            if left > right:
                return

            val = postorder.pop()
            node = TreeNode(val)

            node.right = buildTree_recursive(inorder_indexes[val] + 1, right)
            node.left = buildTree_recursive(left, inorder_indexes[val] - 1)

            return node

        tree = buildTree_recursive(0, len(inorder) - 1)
        return tree


if __name__ == '__main__':
    result = Solution().buildTree2([9, 3, 15, 20, 7], [9, 15, 7, 20, 3])
    print(result)

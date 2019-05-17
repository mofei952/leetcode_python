#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/10/7 15:22
# @File    : 105 Construct Binary Tree from Preorder and Inorder Traversal.py
# @Software: PyCharm

"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
"""

from typing import List

import pytest

from commons import func_test
from tree.tree_node import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """根据先序遍历和中序遍历，构造二叉树"""
        if not preorder or not inorder:
            return None
        val = preorder[0]
        index = inorder.index(val)
        node = TreeNode(val)
        node.left = self.buildTree(preorder[1:index + 1], inorder[:index])
        node.right = self.buildTree(preorder[index + 1:], inorder[index + 1:])
        return node

    def buildTree2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """根据先序遍历和中序遍历，构造二叉树"""
        if not preorder or not inorder:
            return None
        dict = {}
        for i, v in enumerate(inorder):
            dict[v] = i

        def buildTree_recursive(preorder_start, preorder_end, inorder_start, inorder_end):
            if preorder_end < preorder_start or inorder_end < inorder_start:
                return None
            val = preorder[preorder_start]
            node = TreeNode(val)
            index = dict[val]
            node.left = buildTree_recursive(preorder_start + 1, preorder_start + (index - inorder_start), inorder_start,
                                            index - 1)
            node.right = buildTree_recursive(preorder_start + (index - inorder_start) + 1, preorder_end, index + 1,
                                             inorder_end)
            return node

        tree = buildTree_recursive(0, len(preorder) - 1, 0, len(inorder) - 1)
        return tree


@pytest.fixture(scope="module")
def test_data():
    params_list = [
        [[3, 9, 20, 15, 7], [9, 3, 15, 20, 7]],
    ]
    res_list = []
    for params in params_list:
        res_list.append(Solution().buildTree(*params))
    return params_list, res_list, 10000


def test_105(test_data):
    func_test(Solution().buildTree, *test_data)


def test_105_2(test_data):
    func_test(Solution().buildTree2, *test_data)


if __name__ == '__main__':
    pytest.main(['-vv', '--durations=10', '-q', '105 Construct Binary Tree from Preorder and Inorder Traversal.py'])

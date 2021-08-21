#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/22 19:06
# @File    : 113 Path Sum II.py
# @Software: PyCharm

"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:
[
   [5,4,11,2],
   [5,8,4,5]
]
"""

from typing import List

import pytest

from commons import func_test
from tree.binary_tree import TreeNode, create_tree


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right:
            return [[sum]] if root.val == sum else []
        path_list = []
        if root.left:
            t = [[root.val] + path for path in self.pathSum(root.left, sum - root.val)]
            path_list.extend(t)
        if root.right:
            t = [[root.val] + path for path in self.pathSum(root.right, sum - root.val)]
            path_list.extend(t)
        return path_list

    def pathSum2(self, root: TreeNode, sum: int) -> List[List[int]]:
        """short code"""
        if not root:
            return []
        if not root.left and not root.right:
            return [[sum]] if root.val == sum else []
        path_list = self.pathSum(root.left, sum - root.val) + self.pathSum(root.right, sum - root.val)
        path_list = [[root.val] + path for path in path_list]
        return path_list

    path_list = []

    def recursive(self, node, num, path):
        if not node.left and not node.right:
            if node.val == num:
                self.path_list.append(path + [num])
            return
        path.append(node.val)
        if node.left:
            self.recursive(node.left, num - node.val, path)
        if node.right:
            self.recursive(node.right, num - node.val, path)
        path.pop()

    def pathSum3(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        self.path_list = []
        self.recursive(root, sum, [])
        return self.path_list


@pytest.fixture(scope="module")
def test_data():
    params_list = [
        [create_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22],
    ]
    res_list = []
    for params in params_list:
        res_list.append(Solution().pathSum(*params))
    return params_list, res_list, 100000


def test_113(test_data):
    func_test(Solution().pathSum, *test_data)


def test_113_2(test_data):
    func_test(Solution().pathSum2, *test_data)


def test_113_3(test_data):
    func_test(Solution().pathSum3, *test_data)


if __name__ == '__main__':
    # print(Solution().pathSum(TreeNode.create_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22))
    # print(Solution().pathSum2(TreeNode.create_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]), 22))
    pytest.main(['-vv', '--durations=10', '-q', '113 Path Sum II.py'])

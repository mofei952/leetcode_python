#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/9/25 12:08
# @File    : 101 Symmetric Tree.py
# @Software: PyCharm

r"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
"""

import pytest

from commons import func_test
from tree.binary_tree import TreeNode, create_tree


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """二叉树是否对称，先反转左子树，再比较左右子树是否相同"""
        if not root:
            return True
        left2 = self.reverse(root.left)
        return self.same(left2, root.right)

    def reverse(self, node):
        if not node:
            return
        new = TreeNode(node.val)
        new.left, new.right = node.right, node.left
        self.reverse(new.left)
        self.reverse(new.right)
        return new

    def same(self, l, r):
        if not l and not r:
            return True
        elif l and r:
            return l.val == r.val and self.same(l.left, r.left) and self.same(l.right, r.right)
        else:
            return False

    def isSymmetric2(self, root: TreeNode) -> bool:
        """二叉树是否对称，优化后执行速度变快"""
        if not root:
            return True
        return self.symmetric2(root.left, root.right)

    def symmetric2(self, l, r):
        if not l and not r:
            return True
        if l and r:
            return l.val == r.val and self.symmetric2(l.left, r.right) and self.symmetric2(l.right, r.left)
        return False


# pytest -vv --durations=10 -q --tb=line "tree\101 Symmetric Tree.py"
@pytest.fixture(scope="module")
def test_data():
    params_list = [
        [create_tree([1, 2, 2, 3, 4, 4, 3])],
        [create_tree([1, 2, 2, None, 3, None, 3])]
    ]
    res_list = [
        True,
        False
    ]
    return params_list, res_list, 1000000


def test_101(test_data):
    func_test(Solution().isSymmetric, *test_data)


def test_101_2(test_data):
    func_test(Solution().isSymmetric2, *test_data)

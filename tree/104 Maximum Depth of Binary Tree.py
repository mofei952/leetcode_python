#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/4/17 19:11
# @File    : 104 Maximum Depth of Binary Tree.py
# @Software: PyCharm

"""
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""

import random

import pytest

from commons import func_test
from tree.tree_node import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        """数的最大深度"""
        if not root:
            return 0
        queue = [root]
        depth = 0
        while queue:
            depth += 1
            t = []
            for node in queue:
                if node.left:
                    t.append(node.left)
                if node.right:
                    t.append(node.right)
            queue = t
        return depth

    def maxDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth2(root.left), self.maxDepth2(root.right))


@pytest.fixture(scope="module")
def test_data():
    params_list = [
        (TreeNode.create_tree([3, 9, 20, None, None, 15, 7]),),
    ]
    res_list = [
        3,
    ]
    for i in range(0, 299):
        v = TreeNode.create_tree([random.randint(0, i * 10) for i in range(i)])
        params_list.append((v,))
        res_list.append(Solution().maxDepth(v))
    return params_list, res_list, 100


def test_007(test_data):
    func_test(Solution().maxDepth, *test_data)


def test_007_2(test_data):
    func_test(Solution().maxDepth2, *test_data)


if __name__ == '__main__':
    pytest.main(['-vv', '--durations=10', '-q', '--tb=line', '-x', '104 Maximum Depth of Binary Tree.py'])

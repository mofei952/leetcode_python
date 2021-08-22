#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/4/17 19:11
# @File    : 104 Maximum Depth of Binary Tree.py
# @Software: PyCharm

"""
question:
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

import random

import pytest

from commons import func_test
from tree.binary_tree import TreeNode, create_tree


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        nodes = [root]
        depth = 0
        while nodes:
            depth += 1
            new_nodes = []
            for node in nodes:
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
            nodes = new_nodes
        return depth

    def maxDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth2(root.left), self.maxDepth2(root.right))


@pytest.fixture(scope="module")
def test_data():
    params_list = [
        (create_tree([3, 9, 20, None, None, 15, 7]),),
    ]
    res_list = [
        3,
    ]
    for i in range(0, 299):
        v = create_tree([random.randint(0, i * 10) for i in range(i)])
        params_list.append((v,))
        res_list.append(Solution().maxDepth(v))
    return params_list, res_list, 100


def test_104(test_data):
    func_test(Solution().maxDepth, *test_data)


def test_104_2(test_data):
    func_test(Solution().maxDepth2, *test_data)


if __name__ == '__main__':
    pytest.main(['-vv', '--durations=10', '-q', '--tb=line', '-x', '104 Maximum Depth of Binary Tree.py'])

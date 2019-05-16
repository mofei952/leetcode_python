#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/15 19:35
# @File    : 100 Same Tree.py
# @Software: PyCharm

from tree.tree_node import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    print(Solution().isSameTree(TreeNode.create_tree([1, 2, 3]), TreeNode.create_tree([1, 2, 3])))
    print(Solution().isSameTree(TreeNode.create_tree([1, 2, 1]), TreeNode.create_tree([1, 1, 2])))

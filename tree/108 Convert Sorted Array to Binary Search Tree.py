#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/18 19:00
# @File    : 108 Convert Sorted Array to Binary Search Tree.py
# @Software: PyCharm

"""
question:
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
"""

from typing import List

from tree.binary_tree import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        index = len(nums) // 2
        val = nums[index]
        node = TreeNode(val)
        node.left = self.sortedArrayToBST(nums[:index])
        node.right = self.sortedArrayToBST(nums[index + 1:])
        return node

    def sortedArrayToBST2(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        def recursive(start, end):
            if start >= end:
                return None
            mid = (start + end) // 2
            val = nums[mid]
            node = TreeNode(val)
            node.left = recursive(start, mid)
            node.right = recursive(mid + 1, end)
            return node

        tree = recursive(0, len(nums))
        return tree


if __name__ == '__main__':
    Solution().sortedArrayToBST2([-10, -3, 0, 5, 9]).display()

#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/18 19:24
# @File    : 109 Convert Sorted List to Binary Search Tree.py
# @Software: PyCharm

"""
Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted linked list: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5
"""
from typing import List

from linked_list.list_node import ListNode
from tree.binary_tree import TreeNode


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def sortedArrayToBST(nums: List[int]) -> TreeNode:
            if not nums:
                return None
            index = len(nums) // 2
            val = nums[index]
            node = TreeNode(val)
            node.left = sortedArrayToBST(nums[:index])
            node.right = sortedArrayToBST(nums[index + 1:])
            return node

        return sortedArrayToBST(nums)


if __name__ == '__main__':
    print(Solution().sortedListToBST(ListNode.create_linked_list([-10, -3, 0, 5, 9])))

"""
question:
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
"""
import math
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
            # index = math.ceil(len(nums) / 2) - 1
            node = TreeNode(nums[index])
            node.left = sortedArrayToBST(nums[:index])
            node.right = sortedArrayToBST(nums[index + 1:])
            return node

        return sortedArrayToBST(nums)

    def sortedListToBST2(self, head: ListNode) -> TreeNode:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def recursive(left, right):
            if left == right:
                return None
            index = (left + right) // 2
            node = TreeNode(nums[index])
            node.left = recursive(left, index)
            node.right = recursive(index + 1, right)
            return node

        return recursive(0, len(nums))


if __name__ == '__main__':
    Solution().sortedListToBST2(ListNode.create_linked_list([-10, -3, 0, 5, 9])).display()

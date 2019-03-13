#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/3/12 21:28
# @File    : 147 Insertion Sort List.py
# @Software: PyCharm

"""
Sort a linked list using insertion sort.
A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
Algorithm of Insertion Sort:
1.Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
2.At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
3.It repeats until no input elements remain.

Example 1:
Input: 4->2->1->3
Output: 1->2->3->4
Example 2:
Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""
from linked_list.list_node import ListNode


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        """链表插入排序"""
        if not head or not head.next:
            return head
        cur = head.next
        last = head
        while cur:
            t = head
            last_t = None
            while t.val < cur.val:
                last_t = t
                t = t.next
            if cur == t:
                last = cur
                cur = cur.next
            else:
                last.next = cur.next
                if last_t:
                    last_t.next = cur
                else:
                    head = cur
                tt = cur.next
                cur.next = t
                cur = tt
        return head

    def insertionSortList2(self, head: ListNode) -> ListNode:
        """链表插入排序 优化后"""
        if not head or not head.next:
            return head

        root = ListNode(-1)
        root.next = head

        cur = head

        while cur and cur.next:
            val = cur.next.val

            if cur.val < val:
                cur = cur.next
                continue

            t = root
            while t.next and t.next.val < val:
                t = t.next

            new = cur.next
            cur.next = new.next
            new.next = t.next
            t.next = new

        return root.next


if __name__ == '__main__':
    linked_list = ListNode.create_linked_list([4, 2, 1, 3])
    result = Solution().insertionSortList2(linked_list)
    print(result)

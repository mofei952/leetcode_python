#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2018/6/27 17:33
# @File    : 021 Merge Two Sorted Lists.py
# @Software: PyCharm

"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
import pytest

from commons import func_test
from linked_list.list_node import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """合并两个有序链表"""
        cur = head = ListNode(0)
        while l1 or l2:
            if not l1:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            elif not l2:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            elif l1.val < l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            cur = cur.next
        return head.next

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """合并两个有序链表 优化后"""
        cur = head = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return head.next


# pytest -q --tb=line "linked_list\021 Merge Two Sorted Lists.py"
# pytest -vv --durations=10 -q --tb=line "linked_list\021 Merge Two Sorted Lists.py"
# pytest -vv --durations=10 -q --tb=line --junitxml=linked_list\test.xml "linked_list\021 Merge Two Sorted Lists.py"
@pytest.fixture(scope="module")
def test_data():
    params_list = [
        ([2, 3], [1, 2]),
        ([1, 2, 3], [1, 3, 4]),
        ([5, 9, 10], [6, 7, 11, 20]),
    ]
    res_list = [
        '1->2->2->3',
        '1->1->2->3->3->4',
        '5->6->7->9->10->11->20'
    ]
    for i in range(len(params_list)):
        cll = ListNode.create_linked_list
        params_list[i] = cll(params_list[i][0]), cll(params_list[i][1])
    return params_list, res_list, 100000, str


def test_021(test_data):
    func_test(Solution().mergeTwoLists, *test_data)


def test_021_2(test_data):
    func_test(Solution().mergeTwoLists2, *test_data)

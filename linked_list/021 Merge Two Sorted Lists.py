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
# pytest -vv --durations=10 --tb=line "linked_list\021 Merge Two Sorted Lists.py"
# pytest -vv --durations=10 --tb=line --junitxml=linked_list\test.xml "linked_list\021 Merge Two Sorted Lists.py"
@pytest.fixture(scope="module")
def test_data():
    data_list = [
        [2, 3], [1, 2],
        [1, 2, 3], [1, 3, 4],
        [5, 9, 10], [6, 7, 11, 20]
    ]
    test_linked_list = []
    for i in range(len(data_list) // 2):
        l1 = ListNode.create_linked_list(data_list[i * 2])
        l2 = ListNode.create_linked_list(data_list[i * 2 + 1])
        test_linked_list.append((l1, l2))
    return test_linked_list


def speed_test(func, test_data):
    for i in range(100000):
        assert str(func(*test_data[0])) == '1->2->2->3'
        assert str(func(*test_data[1])) == '1->1->2->3->3->4'
        assert str(func(*test_data[2])) == '5->6->7->9->10->11->20'


def test_021(test_data):
    speed_test(Solution().mergeTwoLists, test_data)


def test_021_2(test_data):
    speed_test(Solution().mergeTwoLists2, test_data)

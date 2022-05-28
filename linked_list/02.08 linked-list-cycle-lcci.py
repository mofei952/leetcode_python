"""
question:
https://leetcode.cn/problems/linked-list-cycle-lcci/
"""

import sys


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)

    @staticmethod
    def create(arr):
        if not arr:
            return
        head = ListNode(arr[0])
        node = head
        for val in arr[1:]:
            node.next = ListNode(val)
            node = node.next
        return head


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        nodes = set()
        node = head
        while node:
            if node in nodes:
                return node
            nodes.add(node)
            node = node.next

    def detectCycle2(self, head: ListNode) -> ListNode:
        node = head
        while node:
            if node.val == sys.maxsize:
                return node
            node.val = sys.maxsize
            node = node.next

    def detectCycle3(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast:
            slow = slow.next
            if fast.next is None:
                return
            fast = fast.next.next
            if slow == fast:
                node = head
                while node != slow:
                    slow = slow.next
                    node = node.next
                return node


if __name__ == '__main__':
    head = ListNode.create([3, 2, 0, -4])
    head.next.next.next.next = head.next
    assert Solution().detectCycle3(head) == head.next

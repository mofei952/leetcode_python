"""
quesion:
https://leetcode.com/problems/rotate-list/
"""

from typing import Optional

from linked_list.list_node import ListNode


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        length = 0
        pre_node, node = None, head
        while node:
            length += 1
            pre_node = node
            node = node.next

        n = length - k % length
        if n == length:
            return head

        pre_node.next = head

        node = head
        for _ in range(n - 1):
            node = node.next
        head = node.next
        node.next = None

        return head


if __name__ == '__main__':
    print(Solution().rotateRight(
        ListNode.create_linked_list([1, 2, 3, 4, 5]), 2
    ))
    print(Solution().rotateRight(
        ListNode.create_linked_list([0, 1, 2]), 4
    ))
    print(Solution().rotateRight(
        ListNode.create_linked_list([]), 0
    ))
    print(Solution().rotateRight(
        ListNode.create_linked_list([1]), 5
    ))
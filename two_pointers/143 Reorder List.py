"""
quesion:
https://leetcode.com/problems/reorder-list/
"""

from typing import Optional

from linked_list.list_node import ListNode


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        
        slow = fast = head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow

        prev, curr = mid, mid.next
        while curr.next:
            temp = curr.next.next
            curr.next.next = prev.next
            prev.next = curr.next
            curr.next = temp

        slow, fast = head, mid
        while fast != slow:
            temp = fast.next.next
            fast.next.next = slow.next
            slow.next = fast.next
            slow = fast.next.next
            fast.next = temp

        return head


if __name__ == '__main__':
    print(Solution().reorderList(
        ListNode.create_linked_list([])
    ))
    print(Solution().reorderList(
        ListNode.create_linked_list([1])
    ))
    print(Solution().reorderList(
        ListNode.create_linked_list([1, 2, 3, 4])
    ))
    print(Solution().reorderList(
        ListNode.create_linked_list([1, 2, 3, 4, 5])
    ))

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        odd = ListNode()
        even = ListNode()
        even_head = even

        count = 0
        while node != None:
            count += 1

            if count % 2 == 0:
                even.next = node
                even = even.next
            else:
                odd.next = node
                odd = odd.next

            node = node.next

        odd.next = even_head.next
        even.next = None
        return head

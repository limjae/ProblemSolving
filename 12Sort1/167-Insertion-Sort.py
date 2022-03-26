# https://leetcode.com/problems/insertion-sort-list/
from typing import *
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        sort_done, start = head, ListNode(-1, head)
        while sort_done.next:
            # print(sort_done)
            target = sort_done.next
            prev = start
            compare = start.next

            if target.val >= sort_done.val:
                sort_done = sort_done.next
                continue

            while compare and compare.val <= sort_done.val:
                if target.val < compare.val:
                    sort_done.next = target.next
                    prev.next, target.next = target, compare
                    break
                else:
                    prev, compare = compare, compare.next

            # print(sort_done.next)

        return start.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.com/problems/sort-colors/
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        link_to_arr = []
        while head:
            link_to_arr.append(head.val)
            head = head.next

        link_to_arr.sort(reverse=True)
        last = None
        for i, value in enumerate(link_to_arr):
            last = ListNode(value, last)

        return last
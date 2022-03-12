# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = None

        while node != None:
            tmp = node.next
            node.next = prev
            prev, node = node, tmp

        return prev


# None(prev) node1(node)-> node2(tmp)-> node3-> None
# None <-node1(prev) node2(node)-> node3(tmp)-> None
# None <-node1 <-node2(prev) node3(node)-> None(tmp)
# None <-node1 <-node2 <-node3(prev) None(node)    << 완성!



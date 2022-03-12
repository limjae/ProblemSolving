# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        cur = ListNode()
        head = cur

        while list1 != None and list2 != None:
            if list1.val < list2.val:
                cur.next = list1
                cur, list1 = list1, list1.next
            else:
                cur.next = list2
                cur, list2 = list2, list2.next

        if list1 != None:
            cur.next = list1
        else:
            cur.next = list2

        return head.next


node1 = ListNode(1, None)
head1 = ListNode(0, node1)

node2 = ListNode(2, None)
head2 = ListNode(0, node2)

solution = Solution()
result = solution.mergeTwoLists(head1, head2)
while (result):
    print(result.val)
    result = result.next

# # node1.val =1
# node1 = ListNode(1)
# # node2.val =2
# node2 = ListNode(2)
# # node3.val =3
# node3 = ListNode(3)
#
# node1.next = node2
# node2.next = node3
# # node1 -> node2 -> node3
#
# head = node1
# while head:
#     print(head.val)
#     head = head.next

# [ node1 -> node2 -> node3 ] = l1
# l1.head(출발점)



# cur = ListNode()
#
#
#
# cur -> node1 -> node2  -> node3 .... -> noden -> None
# head
#
#
# return head.next

# l1_node1 = ListNode(1)
# l1_node2 = ListNode(2)
# l1_node3 = ListNode(4)
#
# l1_node1.next = l1_node2
# l1_node2.next = l1_node3
#
# l2_node1 = ListNode(1)
# l2_node2 = ListNode(3)
# l2_node3 = ListNode(4)
#
# l2_node1.next = l2_node2
# l2_node2.next = l2_node3
#
# result = solution.mergeTwoLists(l1_node1, l2_node1)
# while (result):
#     print(result.val)
#     result = result.next

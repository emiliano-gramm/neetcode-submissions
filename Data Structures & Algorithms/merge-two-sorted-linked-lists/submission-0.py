# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode()
        head = output
        l1, l2 = list1, list2

        while(l1 and l2):
            if l1.val < l2.val:
                output.next = l1
                l1 = l1.next
            else:
                output.next = l2
                l2 = l2.next

            output = output.next

        if l1:
            while(l1):
                output.next = l1
                l1 = l1.next
                output = output.next
        if l2:
            while(l2):
                output.next = l2
                l2 = l2.next
                output = output.next

        return head.next
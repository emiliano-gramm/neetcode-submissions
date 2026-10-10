# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        if not head:
            return None
        while(head.next):
            temp = head
            head = head.next
            temp.next = prev
            prev = temp

        temp = head
        head = head.next
        temp.next = prev
        prev = temp

        return temp
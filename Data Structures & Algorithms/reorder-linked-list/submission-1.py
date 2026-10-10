# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reversePointer(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev
            

    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        slow = self.reversePointer(slow)

        while head.next and slow.next:
            temp = head.next
            head.next = slow
            tempSlow = slow.next
            slow.next = temp
            head = temp
            slow = tempSlow
        

    
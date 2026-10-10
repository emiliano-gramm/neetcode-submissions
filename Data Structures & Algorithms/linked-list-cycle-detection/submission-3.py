# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dic = {}

        if not head:
            return False

        slow = head
        fast = head.next

        while(slow != fast and slow and fast):
            if not fast.next or not fast.next.next:
                return False 
            slow = slow.next
            fast = fast.next.next

        if slow == fast:
            return True

        return False
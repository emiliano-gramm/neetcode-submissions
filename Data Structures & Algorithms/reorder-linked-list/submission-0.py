# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        i = 0
        while head:
            temp = head
            nHead = head.next
            while temp.next and temp.next.next:
                temp = temp.next
                if temp.next:
                    continue
            if temp.next:
                head.next = ListNode(temp.next.val)
                print(temp.next.val)
                temp.next = None
            else:
                break
            if not head.next:
                head.next = nHead
                break
            head.next.next = nHead
            head = head.next.next
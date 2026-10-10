# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        q = collections.deque()
        dummyNode = ListNode(None)
        dummyNode.next = head
        head = dummyNode

        while head:
            q.append(head)
            if len(q) > n + 1:
                q.popleft()
            if head.next:
                head = head.next
            else:
                prevRid = q.popleft()
                rid = q.popleft()
                prevRid.next = rid.next
                rid.next = ListNode(None)
                return dummyNode.next

        return dummyNode.next
            
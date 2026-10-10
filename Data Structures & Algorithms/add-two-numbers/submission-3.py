# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        q = collections.deque()
        final = []

        takeover = 0
        dummyNode = ListNode(0, None)

        while l1 and l2:
            val = l1.val+l2.val
            print(val)
            if takeover > 0 and val > 9:
                val = (val+1) % 10
                n = ListNode(val)
            elif takeover > 0:
                val = (val+1) % 10
                n = ListNode(val)
                takeover = 0
            elif val > 9:
                val %= 10
                takeover += 1
                n = ListNode(val)
            else:
                n = ListNode(val)

            if not dummyNode.next:
                dummyNode.next = n
            else:
                prevN = q.pop()
                prevN.next = n
            q.append(n)
            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val
            if takeover > 0:
                if val+1 > 9:
                    val = (val+1) % 10
                else:
                    val = (val+1) % 10
                    takeover = 0
            n = ListNode(val)
            prevN = q.pop()
            prevN.next = n
            q.append(n)
            l1 = l1.next

        while l2:
            val = l2.val
            if takeover > 0:
                if val+1 > 9:
                    val = (val+1) % 10
                else:
                    val = (val+1) % 10
                    takeover = 0
            n = ListNode(val)
            prevN = q.pop()
            prevN.next = n
            q.append(n)
            l2 = l2.next
        
        if takeover > 0:
            n = ListNode(1)
            prevN = q.pop()
            prevN.next = n
        
        return dummyNode.next

        
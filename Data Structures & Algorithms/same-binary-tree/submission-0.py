# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        qP = collections.deque()
        qQ = collections.deque()

        qP.append(p)
        qQ.append(q)

        while (qP and qQ):
            valP = qP.popleft()
            valQ = qQ.popleft()
            if not valP and valQ:
                return False
            if not valQ and valP:
                return False
            if not valQ and not valP:
                continue
            if valP.val != valQ.val:
                return False
            qP.append(valP.left)
            qQ.append(valQ.left)
            qP.append(valP.right)
            qQ.append(valQ.right)

        return True
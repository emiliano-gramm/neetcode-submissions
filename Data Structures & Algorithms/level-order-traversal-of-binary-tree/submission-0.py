# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        container = []
        q = deque()

        q.append(root)

        def getLevelToCont(cQ):
            tmpCont = []
            tmpQ = deque()
            while cQ:
                obj = cQ.popleft()
                if obj:
                    left = obj.left
                    right = obj.right
                    tmpCont.append(obj.val)
                    tmpQ.append(left)
                    tmpQ.append(right)
            return tmpCont, tmpQ
        
        while q:
            tmp, q = getLevelToCont(q)
            if tmp:
                container.append(tmp)
        
        return container
        



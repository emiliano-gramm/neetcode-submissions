# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        q = deque()

        q.append(root)
        result = []
        while q:
            run = []
            for i in range(len(q)):
                run.append(q.popleft())
            
            values = []
            for i in range(len(run)):
                el = run[i]
                if el:
                    q.append(el.left)
                    q.append(el.right)
                    values.append(el.val)
            if values:
                result.append(values)
        
        return result



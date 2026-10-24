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
        
        cont = defaultdict(list)
        q = deque()
        level = 0
        q.append((root, level))
        size = 0
        while q:
            el = q.popleft()
            if el[0]:
                if el[0].left:
                    q.append((el[0].left, el[1]+1))
                if el[0].right:
                    q.append((el[0].right, el[1]+1))
                cont[el[1]].append(el[0].val)
                if el[1] > size:
                    size = el[1]

        ans = [[] for _ in range(size+1)]
        for key, val in cont.items():
            ans[key] = val
        
        return ans



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        if not root:
            return 0
        depth = 1
        tempDepth = 1
        q.append((root, depth))
        while q:
            currRoot, depth = q.popleft()
            if currRoot.left:
                tempDepth = depth + 1
                q.append((currRoot.left, tempDepth))
            if currRoot.right:
                tempDepth = depth + 1
                q.append((currRoot.right, tempDepth))
            if tempDepth > depth:
                depth = tempDepth
        
        return depth
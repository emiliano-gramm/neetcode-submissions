# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        d = 1        

        def dfs(node, depth):
            tempDepthLeft, tempDepthRight = depth, depth
            if not node:
                return depth
            if not node.left and not node.right:
                return depth+1
            if node.left:
                tempDepthLeft = dfs(node.left, depth+1)
            if node.right:
                tempDepthRight = dfs(node.right, depth+1)
            
            return max(tempDepthRight, tempDepthLeft)

        d = max(dfs(root.left,d), dfs(root.right,d))
        return d



        """q = collections.deque()
        if not root:
            return 0
        depth = 1
        newDepth = 1
        q.append((root, depth))
        while q:
            currRoot, depth = q.popleft()
            if currRoot.left:
                newDepth = depth + 1
                q.append((currRoot.left, newDepth))
            if currRoot.right:
                newDepth = depth + 1
                q.append((currRoot.right, newDepth))
            depth = newDepth
        
        return depth"""
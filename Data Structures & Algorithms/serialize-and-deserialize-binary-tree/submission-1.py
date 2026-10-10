# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        arr = []
        q = collections.deque()
        q.append(root)
        while q:
            head = q.popleft()
            bValue = str(head.val)
            if head.left:
                bLeft = str(head.left.val)
                q.append(head.left)
            else:
                bLeft = "None"
            if head.right:
                bRight = str(head.right.val)
                q.append(head.right)
            else:
                bRight = "None"
            arr.append(bValue + "#" + bLeft + "#" + bRight + "Node")
        return "".join(arr)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            x = TreeNode(5)
            return x.left
        arr = data.split("Node")
        arr.pop()
        dummyNode = TreeNode(0, None, None)
        q = collections.deque()
        makeNode = True

        print(arr)
        
        for i in range(len(arr)):
            (head, left, right) = arr[i].split("#") # Gives string vals for head,left,right
            if len(q) == 0: #if q is empty (first node) attach it
                q.append(int(head))
                head = q.popleft()
                if left == "None" and right == "None":
                    left = None
                    right = None
                    h = TreeNode(head, left, right)
                elif left == "None":
                    left = None
                    right = TreeNode(int(right))
                    q.append(right)
                    h = TreeNode(head, left, right)
                elif right == "None":
                    left = TreeNode(int(left))
                    q.append(left)
                    right = None
                    h = TreeNode(head, left, right)
                elif left and right:
                    left = TreeNode(int(left))
                    q.append(left)
                    right = TreeNode(int(right))
                    q.append(right)
                    h = TreeNode(head, left, right)
                    
                if not dummyNode.left:
                    dummyNode.left = h
            else:
                head = q.popleft()
                if left == "None" and right == "None":
                    head.left = None
                    head.right = None
                elif left == "None":
                    head.left = None
                    right = TreeNode(int(right))
                    q.append(right)
                    head.right = right
                elif right == "None":
                    left = TreeNode(int(left))
                    q.append(left)
                    head.left = left
                    head.right = None
                elif left and right:
                    left = TreeNode(int(left))
                    q.append(left)
                    head.left = left
                    right = TreeNode(int(right))
                    q.append(right)
                    head.right = right
        
        return dummyNode.left




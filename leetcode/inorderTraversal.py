class ListNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
    
    def inorderTraversal(self,root):
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

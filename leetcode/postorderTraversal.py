#递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

#BFS
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        flag = []
        stack = []
        res = []
        p = root
        while p or stack:
            while p:
                flag.append(0)
                stack.append(p)
                p = p.left
            while stack and flag[-1] == 1:
                flag.pop()
                res.append(stack.pop().val)
            if stack:
                flag[-1] = 1
                p = stack[-1].right
        return res

迭代
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        stack1 = [t1]
        stack2 = [t2]
        while stack1:
            node1 = stack1.pop()
            node2 = stack2.pop()
            node1.val += node2.val
            if node1.left and node2.left:
                stack1.append(node1.left)
                stack2.append(node2.left)
            elif node2.left:
                node1.left = node2.left
            if node1.right and node2.right:
                stack1.append(node1.right)
                stack2.append(node2.right)
            elif node2.right:
                node1.right = node2.right
        return t1

递归

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left,t2.left)
        t1.right= self.mergeTrees(t1.right,t2.right)
        return t1

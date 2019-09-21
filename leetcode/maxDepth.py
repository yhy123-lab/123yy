# 二叉树高度 非递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        head = [root]
        i = 0
        while head:
            next_layer =[]
            i += 1
            for node in head:
                if node.left == None and node.right != None:
                    next_layer.append(node.right)
                if node.right == None and node.left != None:
                    next_layer.append(node.left)
                if node.left != None and node.right != None:
                    next_layer.extend([node.left,node.right])
            head = next_layer
        return i
#递归版本
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            leftDepth = self.maxDepth(root.left)
            rightDepth = self.maxDepth(root.right)
            return max(leftDepth,rightDepth) + 1
        
        

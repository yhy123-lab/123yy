#冒泡排序
x = [5,4,6,3,8,9,1]
def Bubble_sort(x):
    for i in range(len(x)):
        for j in range(i,len(x)):
            if x[i] > x[j]:
                x[i],x[j] = x[j],x[i]
    return x
print(Bubble_sort(x))

#二分查找
x = [1,3,4,6,7,8,9,10,11,12,13]
find = 8
def binary_chop(x,find):
    while len(x) > 1:
        if find > x[len(x)//2]:
            x = x[len(x)//2:len(x)]
        elif find < x[len(x)//2]:
            x = x[0:len(x)//2]
        else:
            return x[len(x)//2]
print(binary_chop(x,find))
      

# 二叉树高度
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

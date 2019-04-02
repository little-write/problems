# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        return self.depth(pRoot) != -1
    def depth(self, pRoot):
        if not pRoot: return 0
        left = self.depth(pRoot.left)
        if left == -1: return -1
        right = self.depth(pRoot.right)
        if right == -1: return -1
        return -1 if abs(left-right)>1 else 1+max(left,right)
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if not pRoot: return True
        return self.helper(pRoot.left, pRoot.right)
    def helper(self, l1, l2):
        if not l1 and not l2:
            return True
        if (l1 and not l2) or (not l1 and l2):
            return False
        return l1.val==l2.val and self.helper(l1.left, l2.right) and self.helper(l1.right, l2.left)
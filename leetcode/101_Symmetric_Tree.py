# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.Symmetric(root.left, root.right)
    def Symmetric(self, l1, l2):
        if not l1 and not l2:
            return True
        if (not l1 and l2) or (not l2 and l1):
            return False
        return l1.val==l2.val and self.Symmetric(l1.left, l2.right) and self.Symmetric(l1.right, l2.left)
        
        
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''时间复杂度O(N)， 空间复杂度O(1)'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        cur1 = root
        cur2 = None
        res = []
        while cur1:
            cur2 = cur1.left
            if cur2:
                while cur2.right and cur2.right!=cur1:
                    cur2 = cur2.right
                if not cur2.right:
                    cur2.right = cur1
                    cur1 = cur1.left
                    continue
                else:
                    cur2.right = None
            res.append(cur1.val)
            cur1 = cur1.right
        return res

        
'''递归'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(root):
            if not root: return
            helper(root.left)
            res.append(root.val)
            helper(root.right)
            
        if not root: return []
        res = []
        helper(root)
        return res
                    
        
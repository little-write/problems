# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        '''
        #也不知道哪里出了问题
        if not root:
            return True
        cur = root.val
        smallest = -sys.maxsize
        largest = sys.maxsize
        if root.left:
            if root.left.val:
                smallest = root.left.val 
          
        if root.right:
            if root.right.val:
                largest = root.right.val  
        
        if smallest >= cur or cur >= largest:
            return False
        return self.isValidBST(root.left) and self.isValidBST(root.right)
        '''  
        def valid(root, smallest, largest):
            if not root:
                return True
            if smallest >= root.val or largest <= root.val:
                return False
            return valid(root.left, smallest, root.val) and valid(root.right, root.val, largest)
        if not root:
            return True
        return valid(root, -sys.maxsize, sys.maxsize)
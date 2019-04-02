# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        def helper(nums):
            if not nums: return [None]
            res = []
            for i, num in enumerate(nums):
                for l in helper(nums[:i]):
                    for r in helper(nums[i+1:]):
                        node = TreeNode(num)
                        node.left = l
                        node.right = r
                        res.append(node)
            return res
        return helper(list(range(1, n+1)))    
        
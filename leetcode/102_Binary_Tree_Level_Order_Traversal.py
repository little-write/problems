# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''递归'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def dfs(root, level, res):
            if not root: return 
            if len(res) < level:
                res.append([])
            res[level-1].append(root.val)
            dfs(root.left, level+1, res)
            dfs(root.right, level+1, res)
        if not root: return []
        res = []
        dfs(root, 1, res)
        return res

'''迭代'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, cur_level = [], [root]
        while cur_level:
            nxt_level, tmp_res = [], []
            for node in cur_level:
                tmp_res.append(node.val)
                if node.left:
                    nxt_level.append(node.left)
                if node.right:
                    nxt_level.append(node.right)
            res.append(tmp_res)
            cur_level = nxt_level
        return res
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    
    def FindPath(self, root, expectNumber):
        # write code here
        res = []
        allres = []
        def dfs(root, target):
            if not root: return []
            res.append(root.val)
            target -= root.val
            if target==0 and not root.left and not root.right:
                allres.append(res[:])
                '''append添加的是引用，后面的pop会清空res？？'''
            dfs(root.left, target)
            dfs(root.right, target)
            res.pop()
        dfs(root, expectNumber)
        return allres
        
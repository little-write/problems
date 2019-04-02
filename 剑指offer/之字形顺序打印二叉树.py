# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        if not pRoot: return []
        cur_level, res, level = [pRoot], [], 0
        while cur_level:
            nxt_level, tmp_res = [], []
            for node in cur_level:
                tmp_res.append(node.val)
                if node.left:
                    nxt_level.append(node.left)
                if node.right:
                    nxt_level.append(node.right)
            if level%2 == 0:
                res.append(tmp_res)
            else:
                tmp_res.reverse()
                res.append(tmp_res)
            level += 1
            cur_level = nxt_level
        return res
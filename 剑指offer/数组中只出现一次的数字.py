# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        if not array: return []
        res = 0
        for num in array:
            res ^= num
        
        idx = self.findFirstOne(res)
        res1, res2 = 0, 0
        for num in array:
            if self.isBit(num, idx):
                res1 ^= num
            else:
                res2 ^= num
        return [res1, res2]
     
    def findFirstOne(self, res):
        idx = 0
        while idx <= 32 and res&1 == 0:
            idx += 1
            res = res >> 1
        return idx
    def isBit(self, num, idx):
        num = num >> idx
        return num&1
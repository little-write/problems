# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index == 0:
            return 0
        p2, p3, p5 = 0, 0, 0
        res = [1 for i in range(index)]
        for i in range(1, index):
            res[i] = min(res[p2]*2, res[p3]*3, res[p5]*5)
            if res[i] == res[p2]*2: p2 += 1
            if res[i] == res[p3]*3: p3 += 1
            if res[i] == res[p5]*5: p5 += 1
        return res[-1]
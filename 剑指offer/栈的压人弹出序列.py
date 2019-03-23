# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV: return False
        tmp = []
        index = 0
        for i in range(len(pushV)):
            tmp.append(pushV[i])
            while tmp and tmp[-1]==popV[index]:
                tmp.pop()
                index += 1
        return len(tmp)==0
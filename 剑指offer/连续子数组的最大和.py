# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        #dp
        res = array[0]
        cur_max = array[0]
        for i in range(1, len(array)):
            cur_max = max(cur_max+array[i], array[i])
            res = max(res, cur_max)
        return res
        '''
        #暴力解法
        res = []
        for i in range(len(array)):
            for j in range(i, len(array)):
                res.append(array[i:j+1])
        maxnum = -sys.maxsize
        for num in res:
            if sum(num)>maxnum:
                maxnum = sum(num)
        return maxnum
        '''
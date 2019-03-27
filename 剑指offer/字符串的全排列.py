# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss: 
            return []
        if len(ss) == 1: 
            return list(ss)
        res = []
        lst = list(ss)
        lst.sort()
        for i in range(len(lst)):
            if i > 0 and lst[i]==lst[i-1]:
                continue
            temp = self.Permutation(''.join(lst[:i])+''.join(lst[i+1:]))
            for j in temp:
                res.append(lst[i]+j)
        return res
        
        
        
        '''
        def isduplicate(ss, n, t):
            while n < t:
                if ss[n] == ss[t]:
                    return True
                n += 1
            return False
        def swap(ss, i, j):
            if i == j: return
            tmp = ss[j]
            ss[j] = ss[i]
            ss[i] = tmp
        def helper(ss, n, size, result):
            if n == size-1: 
                result.append("".join(ss))
                return
            for i in range(n, size):
                if isduplicate(ss, n, i):
                    continue
                swap(ss, i, n)
                helper(ss, n+1, size, result)
                swap(ss, i, n)
        n = 0
        result = []
        size = len(ss)
        ss = list(ss)
        helper(ss, n, size, result)
        return result
        '''   
        
            
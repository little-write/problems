# -*- coding:utf-8 -*-
'''
基于快排  O(n)
'''
import random
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        A = tinput
        n = len(A)
        if n <= 0 or k > n or k <= 0:
            return []
        start, end = 0, n-1
        m = self._partition(A, start, end)
        while m!=k:
            if m > k:
                end = m - 1
                m = self._partition(A, start, end)
            else:
                start = m+1
                m = self._partition(A, start, end)
        res = A[:k]
        res.sort()
        return res
    def _partition(self, A, start, end):
        j = start
        if start<end:
            pivot = random.randint(start, end)
            A[pivot], A[start] = A[start], A[pivot]   
            for i in range(start+1, end+1):
                if A[i] < A[start]:
                    j += 1
                    A[j], A[i] = A[i], A[j]
            A[start], A[j] = A[j], A[start]
        return j

# -*- coding:utf-8 -*-
'''
基于堆排序
'''
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        A = tinput
        n = len(tinput)
        if n <= 0 or k > n or k <= 0:
            return []
        for i in range((k-1)//2,-1,-1):
            self.adjustHeap(A, i, k-1)
        for j in range(k, n):
            if A[j] < A[0]:
                A[j], A[0] = A[0], A[j]
                self.adjustHeap(A, 0, k-1)
        res = A[:k]
        res.sort()
        return res
    def adjustHeap(self, A, i, k):
        while True:
            maxPos = i
            if 2*i+1<=k and A[maxPos]<A[2*i+1]:
                maxPos = 2*i+1
            if 2*i+2<=k and A[maxPos]<A[2*i+1]:
                maxPos = 2*i+2
            if maxPos == i:
                break
            A[i], A[maxPos] = A[maxPos], A[i]
            i = maxPos   #不能忘记
        
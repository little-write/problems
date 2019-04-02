# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array: return []
        left, right = 0, len(array)-1
        res = []
        while left < right:
            if array[left] + array[right] > tsum:
                right -= 1
            elif array[left] + array[right] < tsum:
                left += 1
            else:
                return [array[left], array[right]]
        return []
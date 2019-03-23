# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray: return
        lst = rotateArray
        low, mid, high = 0, 0, len(lst)-1
        min_val = lst[0]
        if lst[low] < lst[high]:
            return lst[low]
        while low < high:
            if (high-low)==1:
                mid = high
                break
            mid = low+(high-low)//2
            if lst[mid] == lst[low] and lst[mid] == lst[high]:
                for i in range(len(lst)):
                    if lst[i]< min_Val:
                        min_val = lst[i]
                return min_val
            elif lst[mid] >= lst[low]:
                low = mid
            elif lst[mid] <= lst[high]:
                high = mid
        return lst[mid]
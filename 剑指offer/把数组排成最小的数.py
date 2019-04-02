# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers: return ""
        numbers = list(map(str, numbers))
        numbers.sort(cmp = lambda x,y:cmp(x+y, y+x))
        return "".join(numbers).lstrip("0") or "0"
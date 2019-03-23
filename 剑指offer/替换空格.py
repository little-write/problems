# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        space_sum = 0
        for i in s:
            if i == " ":
                space_sum += 1
        new_str = (len(s)+2*space_sum) * [None]
        index_s, index_new = len(s)-1, len(new_str)-1
        while index_new >= 0 and index_s <= index_new:
            if s[index_s] == " ":
                new_str[index_new-2: index_new+1] = ["%", "2", "0"]
                index_new -= 3
                index_s -= 1
            else:
                new_str[index_new] = s[index_s]
                index_new -= 1
                index_s -= 1
        return "".join(new_str)
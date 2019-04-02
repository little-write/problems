# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        cur1 = pHead1
        cur2 = pHead2
        while cur1 != cur2:
            cur1 = cur1.next if cur1 else pHead2
            cur2 = cur2.next if cur2 else pHead1
        return cur1
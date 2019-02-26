# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        '''
        1. 计算size  标记tail
        2. k可能比size大，取余，注意取余后k的大小
        3. 用单指针或双指针移动到距末端kth
        '''
        if not head or k == 0:
            return head
        size = 0
        cur = tail = head
        while cur:
            size += 1
            tail = cur
            cur = cur.next
        
        k = k % size
        if k == 0:
            return head    #必要
        
        tmp = self.findLastKth(head, k, size)
        Last_k = tmp.next
        tmp.next = None
        tail.next = head
        return Last_k
    
    def findLastKth(self, head, k, size):
        for i in range(size-k-1):
            head = head.next
        return head
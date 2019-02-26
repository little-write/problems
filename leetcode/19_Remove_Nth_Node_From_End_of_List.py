# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = r = dummy = ListNode(-1)
        dummy.next = head                   
        for i in range(n):
            if r.next:
                r = r.next
            else:
                return
        
        while r.next:
            r = r.next
            l = l.next
        
        l.next = l.next.next
        return dummy.next
'''
1. 快慢指针
2. dummy head 因为删除的可能是head指针
'''
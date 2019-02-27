# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or m==n:
            return head
        dummy = pre = ListNode(None)
        dummy.next = head
        for i in range(m-1):
            pre = pre.next
        tail = pre.next
        
        for i in range(n-m):
            tmp = pre.next
            pre.next = tail.next
            tail.next = tail.next.next
            pre.next.next = tmp
        return dummy.next
        
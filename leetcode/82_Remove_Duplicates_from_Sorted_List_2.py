# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
        #时间复杂度O(N)， 空间复杂度O(N)
        head_cp = head
        duplicates = {}
        while head:
            while head.next and head.val == head.next.val:
                duplicates[head.val] = 1
                head.next = head.next.next
            head = head.next
        
        dummy = pre = ListNode(None)
        pre.next = head
        while head_cp:
            if head_cp.val not in duplicates:
                pre.next = head_cp
                pre = pre.next
            head_cp = head_cp.next
        pre.next = None
        return dummy.next
        '''
        '''#2
        dummy = pre = cur = ListNode(None)
        while head:
            while head and ((pre.val==head.val) or (head.next and head.next.val==head.val)):
                pre = head
                head = head.next
            cur.next = head
            cur = cur.next
            if head:
                head = head.next
        return dummy.next
        '''
        #递归
        if not head:
            return None
        nxt, is_dup = head.next, False
        while nxt and head.val == nxt.val:
            nxt = nxt.next
            is_dup = True
        head.next = self.deleteDuplicates(nxt)
        return head.next if is_dup else head
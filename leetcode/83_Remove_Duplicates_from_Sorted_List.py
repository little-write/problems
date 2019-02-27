# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
        #1
        if not head:
            return 
        dummy = pre = ListNode(None)
        while head:
            if head.val == pre.val:
                if not head.next:
                    pre.next = None
            else:
                pre.next = head
                pre = pre.next
            head = head.next
        return dummy.next
        '''
        #2
        dummy = head
        while head:
            while head.next and head.val == head.next.val:
                head.next = head.next.next
            head = head.next
        return dummy
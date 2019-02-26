# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        '''
        #loop做
        if not head or not head.next:
            return head
        dummy = cur = ListNode(-1)
        dummy.next = head
        while cur.next and cur.next.next:
            next_one, next_two, next_three = cur.next, cur.next.next, cur.next.next.next
            cur.next = next_two
            next_two.next = next_one
            next_one.next = next_three
            cur = next_one
        return dummy.next
        '''
        #递归做
        if not head or not head.next:
            return head
        tmp = head.next
        head.next = self.swapPairs(head.next.next)
        tmp.next = head
        return tmp
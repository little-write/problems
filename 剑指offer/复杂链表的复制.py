# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        '''
        1、复制每个节点，如：复制节点A得到A1，将A1插入节点A后面
        2、遍历链表，A1->random = A->random->next;
        3、将链表拆分成原链表和复制后的链表
        '''
        if not pHead: return None
        pNode = pHead
        while pNode:
            tmp = RandomListNode(pNode.label)
            tmp.next = pNode.next
            pNode.next = tmp
            pNode = tmp.next
        
        pNode = pHead
        while pNode:
            pClone = pNode.next
            if pNode.random:
                pClone.random = pNode.random.next
            pNode = pClone.next
        
        pNode = pHead
        pClone = pHead.next
        while pNode.next:
            tmp = pNode.next
            pNode.next = tmp.next
            pNode = tmp
        return pClone
        
# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        '''
        BST的后序序列的合法序列是，对于一个序列S，最后一个元素是x （也就是根），如果去掉最后一个元素的序列为T，
        那么T满足：T可以分成两段，前一段（左子树）小于x，后一段（右子树）大于x，且这两段（子树）都是合法的后序序列。
        完美的递归定义 。
        '''
        if not sequence: return False
        root = sequence[-1]
        for i in range(len(sequence)):
            if sequence[i] > root:
                break
        for j in range(i, len(sequence)):
            if sequence[j] < root:
                return False
        left, right = True, True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        if j < len(sequence)-1:
            right = self.VerifySquenceOfBST(sequence[i+1:])
        return left and right
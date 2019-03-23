# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if not matrix: return None
        lst = []
        top, bottom, left, right = 0, len(matrix)-1, 0, len(matrix[0])-1
        while top<=bottom and left<=right:
            for i in range(left, right+1):
                lst.append(matrix[top][i])
            top += 1
            for i in range(top, bottom+1):
                lst.append(matrix[i][right])
            right -= 1
            if top <= bottom:   #判断是否是一行或者一列
                for i in range(right, left-1, -1):
                    lst.append(matrix[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top-1, -1):
                    lst.append(matrix[i][left])
                left += 1
        return lst
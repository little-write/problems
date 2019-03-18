# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.minstack == [] or node < self.min():
            self.minstack.append(node)
        else:
            self.minstack.append(self.min())        
    def pop(self):
        # write code here
        if self.stack == []:
            return None
        self.stack.pop()
        self.minstack.pop()        
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.minstack[-1]
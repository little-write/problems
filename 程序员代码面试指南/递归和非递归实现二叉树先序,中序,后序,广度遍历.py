# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 21:18:56 2019

@author: qwer_mt
"""
'''
递归实现二叉树的前序，中序，后序遍历
'''
# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def pre_order(root):
    if not root: return
    print(root.val)
    pre_order(root.left)
    pre_order(root.right)
    
def in_order(root):
    if not root: return
    in_order(root.left)
    print(root.val)
    in_order(root.right)
    
def pos_order(root):
    if not root: return
    pos_order(root.left)
    pos_order(root.right)
    print(root.val)
    
    
'''
非递归实现二叉树的前序，中序，后序，广度遍历
'''
#前序，栈，先压入右子节点，再压入左子节点
def preOrder(root):
    if not root: return
    res = []
    stack = []
    stack.append(root)
    while len(stack) > 0:
        tmp = stack.pop()
        res.append(tmp.val)
        if tmp.right:
            stack.append(tmp.right)
        if tmp.left:
            stack.append(tmp.left)
    return res

#中序，栈，遍历完左边界，返回，向右，注意条件null
def inOrder(root):
    if not root: return
    stack = []
    res = []
    while len(stack)>0 or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            tmp = stack.pop()
            res.append(tmp.val)
            root = tmp.right
    return res

#后序 两个栈
def posOrder(root):
    if not root: return
    res = []
    stack1 = []
    stack2 = []
    stack1.append(root)
    while len(stack1)>0:
        tmp = stack1.pop()
        stack2.append(tmp.val)
        if tmp.left:
            stack1.append(tmp.left)
        if tmp.right:
            stack1.append(tmp.right)
    res = stack2[::-1]
    return res

#层次遍历 队列
def bfs(root):
    if not root: return
    queue = []
    res = []
    queue.append(root)
    while len(queue) > 0:
        tmp = queue.pop(0)
        res.append(tmp.val)
        if tmp.left:
            queue.append(tmp.left)
        if tmp.right:
            queue.append(tmp.left)
    return res





























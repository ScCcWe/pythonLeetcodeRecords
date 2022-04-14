# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: BinaryTree.py
# author: ScCcWe
# time: 2022/3/3 2:04 下午
class BinaryTree:
    def __init__(self, root, left=None, right=None):
        self.value = root
        self.left = left
        self.right = right

    def __repr__(self):
        return f"node-{self.value}"


# t = BinaryTree(1)
# t.left = BinaryTree(2)
# t.right = BinaryTree(3)
#
# t.left.left = BinaryTree(4)
# t.left.right = BinaryTree(5)
#
# t.right.left = BinaryTree(6)


t = BinaryTree(1)
t.left = BinaryTree(2)
t.right = BinaryTree(5)

t.left.left = BinaryTree(3)
t.left.right = BinaryTree(4)

t.right.left = BinaryTree(6)

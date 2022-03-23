# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: 答案.py
# author: ScCcWe
# time: 2022/3/23 10:00 上午
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.s = set()

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root is None:
            return False
        if k - root.val in self.s:
            return True
        self.s.add(root.val)
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)


if __name__ == '__main__':
    tree = TreeNode(1)
    tree.left = TreeNode(1)

    print(Solution().findTarget(tree, 2))

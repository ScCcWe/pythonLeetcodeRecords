# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: dfs.py
# author: ScCcWe
# time: 2022/3/23 9:46 上午
"""
653. 两数之和 IV - 输入 BST
给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

值得注意的点，因为是二叉搜索树，所以不需要考虑相同的值；
且题目进行了简化，不需要连接的两个数
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    node_set = set()

    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return

        self.node_set.add(root.val)
        self.dfs(root.left)
        self.dfs(root.right)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.dfs(root)

        if len(self.node_set) < 2:
            return False

        for item in self.node_set:
            target = k - item
            if target in self.node_set:
                return True

        return False


if __name__ == '__main__':
    tree = TreeNode(1)

    print(Solution().findTarget(tree, 2))

# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: dfs.py
# author: ScCcWe
# time: 2022/3/23 9:46 上午
"""
653. 两数之和 IV - 输入 BST
给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

分析：
    二叉搜索树的定义：
        一棵空树或者具有下列性质的二叉树
            1）若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值
            2）若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值
            3）任意节点的左右子树也分别为二叉搜索树

    根据定义可知，二叉搜索树root中是不会有相同值的！这样题目其实简化了

    且题目进行了简化，不需要连接的两个数
"""
import copy
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    node_list: List[int] = []

    def dfs(self, root: TreeNode):
        if not root:
            return
        self.node_list.append(root.val)
        self.dfs(root.left)
        self.dfs(root.right)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """"""

        """遍历树"""
        self.dfs(root)

        """根据遍历结果进行判断"""
        for index, item in enumerate(self.node_list):
            target = k - item
            compare_list = copy.deepcopy(self.node_list)
            compare_list = compare_list[:index] + compare_list[index + 1:]
            if target in compare_list:
                return True

        return False


if __name__ == '__main__':
    tree = TreeNode(1)

    print(Solution().findTarget(tree, 2))

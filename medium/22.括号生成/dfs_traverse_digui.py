# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: dfs_traverse_digui.py
# author: ScCcWe
# time: 2022/3/3 2:03 下午
from typing import List

from BinaryTree import BinaryTree, t

result_list = []


# 回顾一下DFS（按照先根顺序）
def dfs_first_root(tree: BinaryTree) -> List:
    if not tree:
        return []

    result_list.append(tree.value)
    dfs_first_root(tree.left)
    dfs_first_root(tree.right)

    return result_list


if __name__ == '__main__':
    result = dfs_first_root(t)
    print(result)

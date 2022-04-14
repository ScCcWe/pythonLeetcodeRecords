# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: dfs_traverse_common.py
# author: ScCcWe
# time: 2022/3/3 1:44 下午
from typing import List

from BinaryTree import BinaryTree, t


# 回顾一下DFS（按照先根顺序）
def dfs_root_first(tree: BinaryTree) -> List:
    if not tree:
        return []

    cur_node = tree
    stack = []

    result_list = []

    while stack or cur_node:
        if not cur_node:
            cur_node = stack.pop(-1)

        print(cur_node.value)
        result_list.append(cur_node.value)

        if cur_node.right:
            stack.append(cur_node.right)

        cur_node = cur_node.left

    return result_list


if __name__ == '__main__':
    result = dfs_root_first(t)
    print(result)

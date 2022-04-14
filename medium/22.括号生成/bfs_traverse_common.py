# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: bfs_traverse_common.py
# author: ScCcWe
# time: 2022/3/3 2:45 下午
from BinaryTree import BinaryTree, t


def bfs_traverse(tree: BinaryTree):
    queue = [tree]

    while queue:
        cur_node = queue.pop(0)
        print(cur_node.value)

        if cur_node.left:
            queue.append(cur_node.left)

        if cur_node.right:
            queue.append(cur_node.right)


if __name__ == '__main__':
    bfs_traverse(t)

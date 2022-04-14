# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: 590n叉树的后序遍历.N叉树的后序遍历.py
# author: ScCcWe
# time: 2022/3/12 8:51 下午
"""
590n叉树的后序遍历. N 叉树的后序遍历

给定一个 n叉树的根节点root，返回 其节点值的 后序遍历 。

n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val

        self.children = children

    def __repr__(self):
        return f"node{str(self.val)}"


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result_list = []

        def dfs(node):
            if not node:
                return

            if node.children:
                for cur_node in node.children:
                    dfs(cur_node)
            result_list.append(node.val)

        dfs(root)

        return result_list


if __name__ == '__main__':
    # [1,null,3,2,4,null,5,6]
    tree = Node(1)
    node3 = Node(3)
    node2 = Node(2)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    tree.children = [node3, node2, node4]
    node3.children = [node5, node6]

    print(Solution().postorder(tree))

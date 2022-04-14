# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: 二叉树的所有路径.py
# author: ScCcWe
# time: 2022/3/15 10:43 上午
import copy


class BinTree(object):
    def __init__(self, root, left=None, right=None):
        self.val = root
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node-{str(self.val)}"


class Solution(object):

    def get_all_path(self, tree: BinTree):
        if not tree:
            return

        # 遍历
        queue = [tree]

        # 路径
        path_list = []  # 所有路径
        path_queue = [[tree.val]]  # 当前节点路径

        while queue:
            cur_node = queue.pop(0)
            cur_path = path_queue.pop(0)

            if not cur_node.left and not cur_node.right:
                path_list.append(cur_path)
            else:

                if cur_node.left:
                    queue.append(cur_node.left)

                    # 收集，这里一定要使用copy，因为list是全局值传递
                    cur_path_cp = copy.deepcopy(cur_path)
                    cur_path_cp.append(cur_node.left.val)
                    path_queue.append(cur_path_cp)

                if cur_node.right:
                    queue.append(cur_node.right)

                    cur_path_cp = copy.deepcopy(cur_path)
                    cur_path_cp.append(cur_node.right.val)
                    path_queue.append(cur_path_cp)

        return path_list


if __name__ == '__main__':
    t = BinTree(1)
    t.left = BinTree(2)
    t.left.left = BinTree(4)
    t.left.right = BinTree(5)

    t.right = BinTree(3)

    res = Solution().get_all_path(t)
    print(res)

# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: 22.括号生成. 括号生成_bfs.py
# author: ScCcWe
# time: 2022/3/3 11:14 上午

"""
22.括号生成. 括号生成

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

此解法为bfs + 剪枝

"""
from typing import List
from collections import Counter


class Solution:

    def large_than_half(self, node_str, n):
        # 只有此时节点的长度大于半数时，才有下面的比较
        if len(node_str) >= int(2 * n / 2) + 1:

            # 比较是否有过半的一种类型str
            counter_node = Counter(node_str)
            for key in counter_node:
                if counter_node[key] > 2 * n / 2:  # 5 / 2 = 2.5（python3
                    return True

        else:
            return False

    def dis_if_collect_by_replace(self, node_str, n):
        for _ in range(n):
            node_str = node_str.replace("()", "")

        return True if node_str == "" else False

    def generateParenthesis(self, n: int) -> List[str]:
        result_list = []

        # 每一个节点可以选择的str
        enum_str_list = ["(", ")"]

        # 剪枝
        # 初始值看似有两种："(", ")"，但是实际能行的就只有一种"("
        queue = ["("]

        while queue:

            cur_node = queue.pop(0)

            # 剪枝
            # 如果一种str超过半数，则一定不满足；如：n=2时，"((("就一定不满足
            #   那么下面的层序遍历，也就不要进行了；
            if self.large_than_half(cur_node, n):
                continue

            # 长度满足，收集起来
            if len(cur_node) == 2 * n:
                if self.dis_if_collect_by_replace(cur_node, n):
                    result_list.append(cur_node)

            # 长度不满足，说明还没有到叶子节点；继续层序遍历
            else:
                for enum_str in enum_str_list:
                    queue.append(cur_node + enum_str)

        return result_list


if __name__ == '__main__':
    result = Solution().generateParenthesis(3)
    print(result)

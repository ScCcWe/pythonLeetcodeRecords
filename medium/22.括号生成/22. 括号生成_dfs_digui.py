# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: 22.括号生成. 括号生成_bfs.py
# author: ScCcWe
# time: 2022/3/3 11:14 上午

"""
22.括号生成. 括号生成

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。

典型的DFS题

"""
from typing import List


class Solution:
    result_list = []

    def generateParenthesis(self, n: int) -> List[str]:

        self.dfs_func(n, n, "")

        return self.result_list

    def dfs_func(self, l: int, r: int, cur_node):
        # 左右括号都不剩余了，递归终止
        if l == 0 and r == 0:
            self.result_list.append(cur_node)
            return

        # 如果左括号还剩余的话，可以拼接左括号
        if l > 0:
            self.dfs_func(l - 1, r, cur_node + "(")

        # 如果右括号剩余多于左括号剩余的话，可以拼接右括号
        if r > l:
            self.dfs_func(l, r - 1, cur_node + ")")


if __name__ == '__main__':
    result = Solution().generateParenthesis(2)
    print(result)

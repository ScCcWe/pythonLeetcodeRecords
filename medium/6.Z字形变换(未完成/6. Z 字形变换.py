# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: 6. Z 字形变换.py
# author: ScCcWe
# time: 2022/3/3 10:31 上午



"""
4行

第一行0：
    numRows + （numRows - 1）- 2 - 2 * 0
    4 + 3 -1 = 5

第二行1：
    周期一：
        numRows + （numRows - 1）- 2 - 2 * 1；
        5 - 2 = 3

    周期二：
        5 - 3 - 1 = 2

第三行2：
    周期一：
        numRows + （numRows - 1）- 2 - 2 * 2
        5 - 4 = 1
    周期二：
        5 - 1 - 1 = 3

最后行3：
    numRows + （numRows - 1）- 2 - 2 * 0
    5

"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:

        result_list = []

        for line_level in range(numRows):
            jump_interval = 2 * numRows - 2

            # for index in range(0, len(s), jump_interval):
            #     # 周期一
            #     result_list.append(s[index + line_level])
            #
            #     # 周期二
            #     if xxx:


        return "".join(result_list)

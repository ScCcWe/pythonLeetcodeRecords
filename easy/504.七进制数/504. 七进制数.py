# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: 504. 七进制数.py
# author: ScCcWe
# time: 2022/3/7 11:28 下午

"""
504. 七进制数

给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。
示例 1:
    输入: num = 100
    输出: "202"

示例 2:
    输入: num = -7
    输出: "-10"

    个人感觉这个负数不对，应该用补码表示

    补码是什么？
        负数(abs+进制转换) -> 原码(取反+1) -> 补码

        例子:
        假设 8位 (还有16位，32位

        -5(abs + 进制转换) -> 0000 0101
        0000 0101(取反)   -> 1111 1010
        1111 1010(+1)    -> 1111 1011

        原码 0000 0101
        反码 1111 1010
        补码 1111 1011
"""


class Solution:
    @staticmethod
    def get_yuan_ma(num):
        collect_list = []
        while num >= 7:
            yushu = num % 7
            collect_list.append(str(yushu))
            num = int(num / 7)
        collect_list.append(str(num))
        return "".join(collect_list[::-1])

    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        if num > 0:
            return self.get_yuan_ma(num)
        else:
            return "-" + self.get_yuan_ma(abs(num))


if __name__ == '__main__':
    print(Solution().convertToBase7(100))
    print(Solution().convertToBase7(-7))
    print(Solution().convertToBase7(-14))

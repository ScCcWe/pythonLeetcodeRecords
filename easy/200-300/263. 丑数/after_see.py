# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: after_see.py
# author: ScCcWe
# time: 2022/3/25 10:43 上午
"""
263. 丑数. 丑数
丑数 就是只包含质因数 2、3 和 5 的正整数。

给你一个整数 n ，请你判断 n 是否为 丑数 。如果是，返回 true ；否则，返回 false 。

"""


class Solution:
    def isUgly(self, n: int) -> bool:
        # 丑数是正整数（正整数不包括0
        if n <= 0:
            return False

        if n == 1:
            return True

        # 2，3，5为质因子，则一定能被2或3或5整除
        while n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
            if n % 2 == 0:
                n = n / 2

            if n % 3 == 0:
                n = n / 3

            if n % 5 == 0:
                n = n / 5

        # 整除结束，如果剩1，就一定是
        if n == 1:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().isUgly(7))

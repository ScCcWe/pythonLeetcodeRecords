# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: self_solution.py
# author: ScCcWe
# time: 2022/3/25 10:42 上午
import copy
import math


class Solution:
    zhi_list = [2, 3, 5]

    def isUgly(self, n: int) -> bool:
        def isZhi(n: int):
            sqrt_n = int(math.sqrt(n))
            for item in range(2, sqrt_n + 1):
                # 可以被整除，不是质数
                if n % item == 0:
                    return False
            # 全都不能被整除，是质数
            return True

        # 丑数是正整数（正整数不包括0
        if n <= 0:
            return False

        # 1, 2, 3, 5, 任意质数
        if n == 1 or n in self.zhi_list or isZhi(n):
            return True

        # 非质数
        for item in self.zhi_list:
            cp_list = copy.deepcopy(self.zhi_list)
            cp_list.remove(item)
            if n % item == 0 and n / item not in cp_list:
                return False

        return True

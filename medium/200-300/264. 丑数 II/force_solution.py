# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: force_solution.py
# author: ScCcWe
# time: 2022/3/25 5:59 下午
class Solution:
    """直接使用for循环，依次判断，超时"""
    def isUglyNumber(self, n: int) -> bool:
        if n == 1:
            return True

        while n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
            if n % 2 == 0:
                n = n / 2
            if n % 3 == 0:
                n = n / 3
            if n % 5 == 0:
                n = n / 5

        if n == 1:
            return True
        else:
            return False

    def nthUglyNumber(self, n: int) -> int:
        for num in range(1, 10 ** 10):
            if self.isUglyNumber(num):
                n = n - 1
                print(f"current value of n: {n}")
                if n == 0:
                    return num


if __name__ == '__main__':
    print(Solution().nthUglyNumber(1690))

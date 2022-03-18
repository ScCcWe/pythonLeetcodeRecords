# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: fib答案.py
# author: ScCcWe
# time: 2022/3/18 4:49 下午
import time


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b

        return a % 1000000007


if __name__ == '__main__':
    start_time = time.time()
    print(Solution().fib(50))
    print(time.time() - start_time)

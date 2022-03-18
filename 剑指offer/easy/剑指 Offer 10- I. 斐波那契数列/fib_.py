# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: fib_.py
# author: ScCcWe
# time: 2022/3/18 4:48 下午
import time


class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.fib(n - 1) + self.fib(n - 2)


if __name__ == '__main__':
    start_time = time.time()
    print(Solution().fib(100))
    print(time.time() - start_time)

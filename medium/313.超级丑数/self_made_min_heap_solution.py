# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: self_made_min_heap_solution.py
# author: ScCcWe
# time: 2022/4/14 9:00 上午
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:

        min_heap = [1]

        for _ in range(n - 1):
            min_heap.sort()
            heap_root = min_heap.pop(0)

            for factor in primes:
                if heap_root * factor not in min_heap:
                    min_heap.append(heap_root * factor)

        return min(min_heap)


if __name__ == '__main__':
    n = 12
    primes = [2, 7, 13, 19]
    print(Solution().nthSuperUglyNumber(n, primes))

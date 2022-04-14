# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: self_made_min_heap_solution.py
# author: ScCcWe
# time: 2022/4/14 9:00 上午
from heapq import heappop, heappush
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        """使用heapq中提供的小根堆操作方法

        heappush 向小根堆插入一个数据
        heappop  从小根堆弹出一个数据（效果同pop，弹出之后，原始堆就没有这个数据了
        """

        # 维护的小跟堆`min_heap`，初始值为1
        min_heap = [1]

        for _ in range(n - 1):
            # 弹出小跟堆的顶，也就是最小值；
            # 用作被乘数
            heap_root = heappop(min_heap)

            for factor in primes:
                if heap_root * factor not in min_heap:
                    heappush(min_heap, heap_root * factor)

        # 只需要执行n-1操作，那么此时形成的小跟堆的堆顶元素就是：第n个丑数
        return heappop(min_heap)


if __name__ == '__main__':
    n = 12
    primes = [2, 7, 13, 19]
    print(Solution().nthSuperUglyNumber(n, primes))

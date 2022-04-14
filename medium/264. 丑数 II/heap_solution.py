# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: heap_solution.py
# author: ScCcWe
# time: 2022/4/13 9:38 上午
from typing import List


class Solution:
    """
    使用小根堆的解法
    """
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1

        factors_list: List[int] = [2, 3, 5]
        min_heap: List[int] = [1]

        # 实际只能执行n-1次；
        # 为什么？
        #   因为n-1次执行完了之后，第n个丑数就是小根堆中最小的，即：堆顶
        #   这样也就不需要再执行了
        for _ in range(n - 1):

            """得到小根堆的堆顶，并将它拿走"""
            # 去重
            min_heap = list(set(min_heap))
            # 从小到大排序
            min_heap.sort()
            # pop出来此时的堆顶值（即：最小值
            small_value = min_heap.pop(0)

            """入堆"""
            for item in factors_list:
                min_heap.append(small_value * item)

        # n-1次执行之后，第n个数，就是堆顶元素值；（也就是最小值
        return min(min_heap)


if __name__ == '__main__':
    print(Solution().nthUglyNumber(2))
    print(Solution().nthUglyNumber(10))
    print(Solution().nthUglyNumber(100))

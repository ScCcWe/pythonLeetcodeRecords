# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: dp_solution(便于理解.py
# author: ScCcWe
# time: 2022/4/14 9:12 上午
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # dp[n]: 第n个丑数
        dp = [0] * (n + 1)

        # 指针表示下一个丑数：当前指针指向的丑数乘以对应的质因数
        # 将指针放在字典中，初始都为0，因为这里是没有直接给pointer_
        pointer_list = [0] * len(primes)

        # 动态维护的，对比数字
        # 总共是4个，
        compare_nums = [1] * len(primes)

        # 这里为什么要从1开始，而不是2
        # 是因为我们需要使用compare_nums，而compare_nums只有第一位是一定正确的，也就是compare_nums[0] = 1
        for dp_index in range(1, n + 1):
            min_value = min(compare_nums)
            dp[dp_index] = min_value

            for factor_index, factor in enumerate(primes):
                if min_value == compare_nums[factor_index]:
                    # 指针位置向右移一位
                    # pointer + 1
                    pointer_list[factor_index] += 1

                    # 取出此时的值，保存在compare_nums; 方便下一次快速对比
                    cur_pointer_num = pointer_list[factor_index]
                    compare_nums[factor_index] = dp[cur_pointer_num] * factor

        return dp[n]


if __name__ == '__main__':
    print(Solution().nthSuperUglyNumber(12, [2, 7, 13, 19]))
    # print(Solution().nthSuperUglyNumber(100, [2, 7, 13, 19]))

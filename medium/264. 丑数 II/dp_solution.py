# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: dp_solution(便于理解.py
# author: ScCcWe
# time: 2022/4/14 11:28 上午
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 第n个丑数：dp[n]
        dp = [0] * (n + 1)

        # 第一个丑数一定是1
        dp[1] = 1

        # 指针表示下一个丑数：当前指针指向的丑数乘以对应的质因数
        # 初始都为1
        pointer_2 = 1
        pointer_3 = 1
        pointer_5 = 1

        # 当 2 <= i <= n
        # dp[n] = min(dp[pointer_2] * 2, dp[pointer_3] * 3, dp[pointer_5] * 5)

        for i in range(2, n + 1):

            dp[i] = min(dp[pointer_2] * 2, dp[pointer_3] * 3, dp[pointer_5] * 5)

            if dp[i] == dp[pointer_2] * 2:
                pointer_2 += 1
            if dp[i] == dp[pointer_3] * 3:
                pointer_3 += 1
            if dp[i] == dp[pointer_5] * 5:
                pointer_5 += 1

        return dp[n]


if __name__ == '__main__':
    print(Solution().nthUglyNumber(10))
    print(Solution().nthUglyNumber(100))

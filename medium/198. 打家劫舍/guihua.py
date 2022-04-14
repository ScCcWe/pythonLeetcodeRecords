# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: guihua.py
# author: ScCcWe
# time: 2022/3/24 10:13 上午
"""

... n-2 n-1 n ...

第n间房, 金额为Sn

    偷窃第n间房（那么n左边的就不能偷窃了，即n-1不能偷窃了；这时候要求最大值，就是n-2的最大值
        sum = sum(n-2) + Sn

    不偷窃第n间房（这时候求最大值，就是n-1的最大值
        sum = sum(n-1)


题目是要求最大金额，也就是max( sum(n-2) + Sn, sum(n-1) )

"""
from typing import List


class Solution:
    ans = 0
    result_list = []

    def rob(self, nums: List[int]):
        size = len(nums)

        if size <= 2:
            return max(nums)

        # 为什么这里：dp = [0] * size
        # 相当于每一个房间都有两种选择，一种是抢劫，一种是不抢；
        # dp[index]代表什么？
        # dp[index]代表的是这一次选择之后(无论是抢还是不抢)，产生的最大金额；
        dp = [0] * size

        # dp[0], dp[1]都是提前可以知道的量
        dp[0] = nums[0]
        print(f"第1间房的最大金额: {dp[0]}\n")

        dp[1] = max(nums[0], nums[1])
        print(f"第2间房的最大金额: {dp[1]}\n")

        for index in range(2, size):  # 从index为2开始（0， 1都是固定的
            print(f"----选择是否偷窃第{index + 1}间房")

            rob_sum_price = nums[index] + dp[index - 2]
            print(f"偷窃后的最大金额是: ", rob_sum_price)

            not_rob_sum_price = dp[index - 1]
            print(f"不偷窃的最大金额是: ", not_rob_sum_price)

            dp[index] = max(rob_sum_price, not_rob_sum_price)
            print(f"----选择完后第{index + 1}间房的最大金额是: {dp[index]}")
            print()

        return dp[-1]


if __name__ == '__main__':
    # print(Solution().rob([1, 2, 3, 1]))
    print(Solution().rob([2, 7, 9, 3, 1]))

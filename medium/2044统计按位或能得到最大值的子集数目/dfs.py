# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: dfs.py
# author: ScCcWe
# time: 2022/3/15 10:16 上午
from typing import List


class Solution:

    answer: int = 0
    target: int = 0
    nums: List[int] = []

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        """
        越或越大，不会变小；

        0 | x = x；


        2 | 5 = 7
        如何计算呢？
        2: 0010
        5: 0101
        --------
           0111 -> 7
        """
        for item in nums:
            self.target = self.target | item

        self.nums = nums

        self.dfs(0, 0)

        return self.answer

    def dfs(self, result: int, index: int):
        # 结束条件优化：当result等于target，其实就可以结束了；因为在继续下去值也不会变了（越或只能越大
        # if result == self.target:
        #     self.answer = self.answer + 1
        #     return

        # 结束条件: 当次运行到结尾
        if index == len(self.nums):
            if result == self.target:
                self.answer = self.answer + 1
            return

        # 每一次移动，可以或下一个位置的值，也可以不或

        # 不或下一个位置的值
        self.dfs(result, index + 1)

        # 或下一个位置的值
        result = result | self.nums[index]
        self.dfs(result, index + 1)


if __name__ == '__main__':
    print(Solution().countMaxOrSubsets([3, 1]))

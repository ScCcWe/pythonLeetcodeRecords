# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: dfs.py
# author: ScCcWe
# time: 2022/3/24 9:50 上午
from typing import List


class Solution:
    ans = 0
    result_list = []

    def dfs(self, nums: List[int]):
        if not nums:
            self.ans = 0
            return

        for index, num in enumerate(nums):
            self.ans += num
            next_nums = nums[: index] + nums[index + 2:]

            if not next_nums:
                self.result_list.append(self.ans)
                self.ans -= num

            self.dfs(next_nums)

    def rob(self, nums: List[int]) -> int:

        self.dfs(nums)

        return max(self.result_list)


if __name__ == '__main__':
    print(Solution().rob([1, 2, 3, 1]))

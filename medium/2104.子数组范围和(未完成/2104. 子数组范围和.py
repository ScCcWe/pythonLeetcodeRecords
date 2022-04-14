# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: 2104.子数组范围和(未完成. 子数组范围和.py
# author: ScCcWe
# time: 2022/3/4 9:03 上午
from typing import List


class Solution:

    def get_list_max_range(self, nums: List[int]):
        return max(nums) - min(nums)

    def subArrayRanges(self, nums: List[int]) -> int:
        ...

# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: 2016增量元素之间的最大差值.py
# author: ScCcWe
# time: 2022/3/3 8:58 上午
from typing import List

"""
给你一个下标从 0 开始的整数数组 nums ，该数组的大小为 n ;

请你计算 nums[j] - nums[i] 能求得的 最大差值 ，其中 0 <= i < j < n 且 nums[i] < nums[j] ;

返回 最大差值 。如果不存在满足要求的 i 和 j ，返回 -1 ;

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-difference-between-increasing-elements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        max_different_list = []

        for index, item in enumerate(nums):
            # i肯定用不到的，因为我们的逻辑，就默认了i < j
            # i = index
            i_value = item
            j_value = max(nums[index:])
            if j_value > i_value:
                max_different_list.append(j_value - i_value)

        if len(max_different_list) > 0:
            return max(max_different_list)

        return -1


if __name__ == '__main__':
    print(Solution().maximumDifference([7, 1, 5, 4]))
    print(Solution().maximumDifference([9, 4, 3, 2]))
    print(Solution().maximumDifference([1, 5, 2, 10]))

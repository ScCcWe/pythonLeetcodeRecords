# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: 599两个列表的最小索引总和.dict解法.py
# author: ScCcWe
# time: 2022/3/14 9:18 上午
from collections import Counter
from typing import List, Tuple


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result_dict: dict = {}

        def get_small_length_list(one: List[str], other: List[str]) -> Tuple[List[str], List[str]]:
            if len(one) > len(other):
                return other, one
            return one, other

        small, big = get_small_length_list(list1, list2)
        for index, item in enumerate(small):
            if item in big:
                index_sum_key = index + big.index(item)

                if index_sum_key not in result_dict:
                    result_dict[index_sum_key] = [item]
                else:
                    result_dict[index_sum_key].append(item)

        # sorted 从小到大排序
        return result_dict[sorted(Counter(result_dict))[0]]


if __name__ == '__main__':
    print(Solution().findRestaurant(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["KFC", "Shogun", "Burger King"]))

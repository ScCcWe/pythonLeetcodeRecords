# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: 599两个列表的最小索引总和.dict解法.py
# author: ScCcWe
# time: 2022/3/14 9:18 上午
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result_dict = {}

        def get_small_length_list(one, other):
            if len(one) > len(other):
                return other, one
            return one, other

        small, big = get_small_length_list(list1, list2)
        for index, item in enumerate(small):
            if item in big:
                index_sum_key = index + big.index(item)

                if len(list(result_dict.keys())) == 0:
                    result_dict[index_sum_key] = [item]
                else:
                    if list(result_dict.keys())[0] > index_sum_key:
                        result_dict.clear()
                        result_dict[index_sum_key] = [item]
                    elif list(result_dict.keys())[0] == index_sum_key:
                        result_dict[index_sum_key].append(item)
                    else:
                        pass

        return result_dict[list(result_dict.keys())[0]]


if __name__ == '__main__':
    print(Solution().findRestaurant(
        ["Shogun", "Tapioca Express", "Burger King", "KFC"],
        ["KFC", "Shogun", "Burger King"]))

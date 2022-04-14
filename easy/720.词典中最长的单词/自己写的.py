# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: 自己写的.py
# author: ScCcWe
# time: 2022/3/17 9:37 上午
from typing import List

"""
题目没有说清楚，一个word是否满足，还需要看在words中，有没有全部的儿子
类似于："yodn" 和 "ewqz"
在 words = ["yo", "ew", "fc", "zrc", "yodn", "fcm", "qm", "qmo", "fcmz", "z", "ewq", "yod", "ewqz", "y"]
"ewqz"虽然字典排序比"yodn"小，但是是不满足的，因为在words中没有"e"
"""


class Solution:
    def longestWord(self, words: List[str]) -> str:
        def dis_satisfied_item_every_son_in_words(satisfied_item: str, words: List[str]):
            for index in range(len(satisfied_item)):
                match_item = satisfied_item[:index + 1]
                if match_item not in words:
                    return False
            return True

        single_word: List[str] = [word for word in words if len(word) == 1]

        filter_words: List[str] = [word for word in words if word[0] in single_word]

        # 按照item的长度，从大到小排序
        filter_words.sort(reverse=True, key=lambda x: len(x))

        satisfy_words = [
            filter_word for filter_word in filter_words
            if dis_satisfied_item_every_son_in_words(filter_word, words)
        ]

        max_len_filter_list = [word for word in satisfy_words if len(word) == len(satisfy_words[0])]

        if not max_len_filter_list:
            return ""
        else:
            if len(max_len_filter_list) == 1:
                return max_len_filter_list[0]
            else:
                max_len_filter_list.sort()  # 从小到大排序（此处是同长度的，从小到大排序，index为0处就是字典顺序最小的；即结果
                return max_len_filter_list[0]


if __name__ == '__main__':
    print(Solution().longestWord(words=["a", "banana", "app", "appl", "ap", "apply", "apple"]))
    print(Solution().longestWord(words=["w", "wo", "wor", "worl", "world"]))
    print(Solution().longestWord(
        words=["yo", "ew", "fc", "zrc", "yodn", "fcm", "qm", "qmo", "fcmz", "z", "ewq", "yod", "ewqz", "y"]))

    print(Solution().longestWord(
        words=["wo", "wor", "worl", "world"]))

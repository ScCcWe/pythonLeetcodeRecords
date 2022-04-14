# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: 答案1.py
# author: ScCcWe
# time: 2022/3/17 2:05 下午
from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        # 顺序：从大到小
        # 先按`x的长度`反着排，然后按照x排；
        words.sort(key=lambda x: (-len(x), x), reverse=True)

        longest = ""
        candidates = {""}
        for word in words:
            if word[:-1] in candidates:
                longest = word
                candidates.add(word)
        return longest


if __name__ == '__main__':
    print(Solution().longestWord(
        words=["a", "banana", "app", "appl", "ap", "apply", "apple"]))

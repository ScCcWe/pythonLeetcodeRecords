# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: 答案2前缀树解法.py
# author: ScCcWe
# time: 2022/3/18 1:53 下午
"""
使用前缀树

"""
from typing import List


class Trie(object):
    def __init__(self):
        self.children = [None] * 26

        self.isEnd = False

    def searchPrefix(self, word: str):
        node = self

        for character in word:
            ch_index = ord(character) - ord("a")
            if not node.children[ch_index]:
                return None
            node = node.children[ch_index]

        return node

    def insert(self, word: str):
        node = self

        for character in word:
            ch_index = ord(character) - ord("a")
            if not node.children[ch_index]:
                node.children[ch_index] = Trie()
            node = node.children[ch_index]

        node.isEnd = True

    def search(self, word: str):
        node = self

        for character in word:
            ch_index = ord(character) - ord("a")
            if not node.children[ch_index] or not node.children[ch_index].isEnd:
                return False
            node = node.children[ch_index]

        return True

    def startswith(self, word: str):
        node = self.searchPrefix(word)
        return True if node else False


class Solution:
    def longestWord(self, words: List[str]) -> str:

        trie_ins = Trie()
        for word in words:
            trie_ins.insert(word)

        longest: str = ""
        for word in words:
            if trie_ins.search(word):
                if len(word) > len(longest):
                    longest = word
                if len(word) == len(longest) and word < longest:
                    longest = word

        return longest


if __name__ == '__main__':
    # ins = Trie()
    # print(ins.insert("apple"))
    # print(ins.startswith("app"))
    # print(ins.search("apple"))
    #
    # print(ins.insert("bottle"))
    # print(ins.search("bottle"))
    # print(ins.startswith("bott"))

    print(Solution().longestWord(words=["a", "banana", "app", "appl", "ap", "apply", "apple"]))
    print(Solution().longestWord(words=["w", "wo", "wor", "worl", "world"]))
    print(Solution().longestWord(
        words=["yo", "ew", "fc", "zrc", "yodn", "fcm", "qm", "qmo", "fcmz", "z", "ewq", "yod", "ewqz", "y"]))

    print(Solution().longestWord(
        words=["wo", "wor", "worl", "world"]))

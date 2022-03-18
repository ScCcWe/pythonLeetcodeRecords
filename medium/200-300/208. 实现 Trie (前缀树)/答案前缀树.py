# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: 答案前缀树.py
# author: ScCcWe
# time: 2022/3/17 2:19 下午
"""
前缀树类似于n叉树

当限定范围为a-z时，是26叉树

"""


class Trie:

    def __init__(self):
        # 26个英文字母
        # ord("z") - ord("a") = 25
        # ord("a") - ord("a") = 0
        self.children = [None] * 26

        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self

        for char in word:
            char_index = ord(char) - ord("a")
            if not node.children[char_index]:
                node.children[char_index] = Trie()
            node = node.children[char_index]

        node.isEnd = True

    def searchPrefix(self, word):
        node = self

        for char in word:
            index = ord(char) - ord("a")
            if not node.children[index]:
                return None
            node = node.children[index]
        return node

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        return True if self.searchPrefix(prefix) else False


def traverse(trie: Trie):
    if not trie:
        return

    if trie.children:
        # print(trie.children)
        for index, node in enumerate(trie.children):
            if node and not trie.isEnd:
                print(chr(index + 97))
                traverse(node)


if __name__ == '__main__':
    # Your Trie object will be instantiated and called as such:
    trie = Trie()
    print(trie.insert("apple"))
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    print(trie.insert("app"))
    print(trie.search("app"))

    traverse(trie)

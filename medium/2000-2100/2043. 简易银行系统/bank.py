# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: bank.py
# author: ScCcWe
# time: 2022/3/18 10:30 上午
from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        # 第n个account 的初始余额是 balance[n - 1]
        # account: 1, 2, 3, ..., n
        # balance: 0, 1, 2, ..., n - 1
        self.balance = balance

        self.n = len(self.balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        """从account1向account2中转账money"""
        if 1 <= account1 <= self.n and 1 <= account2 <= self.n:
            if self.balance[account1 - 1] >= money:
                self.balance[account1 - 1] = self.balance[account1 - 1] - money
                self.balance[account2 - 1] = self.balance[account2 - 1] + money
                return True
            else:
                return False
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        """向账户account中，存款money"""
        if 1 <= account <= self.n:
            # 存款
            self.balance[account - 1] = self.balance[account - 1] + money
            return True
        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        """从账户account中，取款money"""
        if 1 <= account <= self.n:
            if self.balance[account - 1] >= money:
                # 扣款
                self.balance[account - 1] = self.balance[account - 1] - money
                return True
            else:
                return False
        else:
            return False

# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)

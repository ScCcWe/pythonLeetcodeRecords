# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: dp_solution(便于理解.py
# author: ScCcWe
# time: 2022/4/14 9:12 上午
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        """
        为什么可以这样dp？
            因为每一个丑数，一定是由primes中的因质数乘出来的！
                比如：primes=[2, 3, 5]，那么丑数可以是：2*3；2*2*3；2*5；但是2 * 7 这种就一定不行


            我们可以维护三个值：dp[p2]，dp[p3]，dp[p5]；让他们每一次都分别乘上[2, 3, 5]中的一个数
            为什么要维护三个值呢？一个不行吗？只要每次都乘上最小值就行了。
                想法是好的，但是很难实现，首先：
                    因为由质因数得到的丑数不是简单的2 * 3，2 * 4，还可以是2 * 3 * 3 * 5...这样就太麻烦了；

                更加致命的是下面这样：
                    第一次是2, 3, 5；最小为2
                    第二次是3， 5 + 4， 6， 10 -> 3, 5, 4, 6, 10；最小则是4，而不是5！

            但是如果使用三个指针，来维护三个值，每一次都分别乘上对应的factor，那么就很容易表示出第i个丑数：
            dp[i] = min(dp[pointer_2] * 2, dp[pointer_3] * 3, dp[pointer_5] * 5)

            综上知：
                dp[1] = 1

                当 2 <= i <= n
                dp[i] = min(dp[pointer_2] * 2, dp[pointer_3] * 3, dp[pointer_5] * 5)

        ------------------------假设条件----------------------
        n = 12
        primes = [2, 7, 13, 19]

        ------------------------初始(dp[1] = 1是固定的，不计算)----------------------
        col_dict = {
            "2": 1,
            "7": 1,
            "13": 1,
            "19": 1,
        }
        dp[1] = 1

        ------------------------第二轮(dp[2])----------------------
        dp[2] = min(
            dp[col_dict["2"]]  * 2,
            dp[col_dict["7"]]  * 7,
            dp[[col_dict["13"]] * 13,
            dp[[col_dict["19"]] * 19
        ) = min(
            1 * 2,
            1 * 7,
            1 * 13,
            1 * 19,
        ) = 2
        因为
            col_dict["2"] = 1，其对应的factor = 2
            col_dict["2"] * factor = 1 * 2 = 2
        所以
            col_dict["2"] += 1
        那么此时
            col_dict = {
                "2": 2,
                "7": 1,
                "13": 1,
                "19": 1,
            }

        ------------------------第三轮(dp[3])----------------------
        dp[2] = min(
            dp[col_dict["2"]]  * 2,
            dp[col_dict["7"]]  * 7,
            dp[[col_dict["13"]] * 13,
            dp[[col_dict["19"]] * 19
        ) = min(
            2 * 2,
            1 * 7,
            1 * 13,
            1 * 19,
        ) = 4
        因为
            col_dict["2"] = 2，其对应的factor = 2
            col_dict["2"] * factor = 2 * 2 = 4
        所以
            col_dict["2"] += 1
        那么此时
            col_dict = {
                "2": 3,
                "7": 1,
                "13": 1,
                "19": 1,
            }

        ------------------------第四轮(dp[4])----------------------
        dp[2] = min(
            dp[col_dict["2"]]  * 2,
            dp[col_dict["7"]]  * 7,
            dp[[col_dict["13"]] * 13,
            dp[[col_dict["19"]] * 19
        ) = min(
            4 * 2,
            1 * 7,
            1 * 13,
            1 * 19,
        ) = 4
        因为
            col_dict["7"] = 1，其对应的factor = 7
            col_dict["7"] * factor = 1 * 7 = 7
        所以
            col_dict["7"] += 1
        那么此时
            col_dict = {
                "2": 3,
                "7": 2,
                "13": 1,
                "19": 1,
            }

        ...
        """

        # 第n个丑数：dp[n]
        dp = [0] * (n + 1)

        # 第一个丑数一定是1
        # 这里你可能会疑问：从dp[1]开始，那么dp[0]怎么办？
        #   这里的dp[0]不会影响后续代码逻辑，不用管就行。
        dp[1] = 1

        # 指针表示下一个丑数：当前指针指向的丑数乘以对应的质因数
        # 将四个指针放在字典中，初始都为1
        # col_dict = {
        #     "2": 1,
        #     "7": 1,
        #     "13": 1,
        #     "19": 1,
        # }
        col_dict = {}
        for pointer in primes:
            col_dict[str(pointer)] = 1

        for i in range(2, n + 1):
            # 将每一个指针在dp中值乘上对应的数字，然后取出此时的最小值
            min_value = min(
                [
                    dp[col_dict[str(factor)]] * factor
                    for factor in primes
                ]
            )
            dp[i] = min_value

            for factor in primes:
                if min_value == dp[col_dict[str(factor)]] * factor:
                    col_dict[str(factor)] += 1

        return dp[n]


if __name__ == '__main__':
    print(Solution().nthSuperUglyNumber(100, [2, 7, 13, 19]))

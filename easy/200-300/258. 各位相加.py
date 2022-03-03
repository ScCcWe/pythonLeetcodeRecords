# !/usr/bin/env python 
# -*- coding: utf-8 -*-
# file_name: 258. 各位相加.py
# author: ScCcWe
# time: 2022/3/3 9:36 上午


"""
258. 各位相加

给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。

输入: num = 38
输出: 2
解释: 各位相加的过程为：
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
由于2 是一位数，所以返回 2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:

    def addDigits(self, num: int) -> int:

        toge = 0
        for i in str(num):
            toge += int(i)

        if len(str(toge)) != 1:
            # 此处有一个递归的坑
            # 这里一定要return
            return self.addDigits(int(toge))
        else:
            return int(toge)


if __name__ == '__main__':
    print(Solution().addDigits(29))

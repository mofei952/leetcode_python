#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/5/8 19:39
# @File    : 319 Bulb Switcher.py
# @Software: PyCharm

"""
There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb.
On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the i-th round,
you toggle every i bulb. For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Input: 3
Output: 1
Explanation:
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off].

So you should return 1, because there is only one bulb is on.
"""
import pytest

from commons import func_test


class Solution:
    def bulbSwitch(self, n: int) -> int:
        list_ = []
        for i in range(n):
            list_.append((i + 1) % 2)
        for i in range(2, n):
            list_[i:n + 1:i + 1] = list(map(lambda x: 1 - x, list_[i:n + 1:i + 1]))
        return sum(list_)

    def bulbSwitch2(self, n: int) -> int:
        t = 3
        c = 0
        while n > 0:
            n -= t
            c += 1
            t += 2
        return c

    def bulbSwitch3(self, n: int) -> int:
        import math
        return int(math.sqrt(n))


@pytest.fixture(scope="module")
def test_data():
    params_list = []
    res_list = []
    for i in range(1, 100):
        params_list.append((i,))
        res_list.append(Solution().bulbSwitch(i))
    return params_list, res_list, 10000


# def test_319(test_data):
#     func_test(Solution().bulbSwitch, *test_data)


def test_319_2(test_data):
    func_test(Solution().bulbSwitch2, *test_data)


def test_319_3(test_data):
    func_test(Solution().bulbSwitch3, *test_data)


if __name__ == '__main__':
    pytest.main(['-vv', '--durations=10', '-q', '--tb=line', '-x', '319 Bulb Switcher.py'])

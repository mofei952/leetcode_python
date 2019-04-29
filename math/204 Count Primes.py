#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/4/28 20:31
# @File    : 204 Count Primes.py
# @Software: PyCharm

"""
Count the number of prime numbers less than a non-negative number, n.

Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
import math
import pytest

from commons import func_test


class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(2, n):
            flag = True
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    flag = False
            if flag:
                count += 1
        return count

    def countPrimes2(self, n: int) -> int:
        b_list = [False] * 2 + [True] * (n - 2)
        for i in range(2, n):
            if not b_list[i]:
                continue
            for j in range(i * i, n, i):
                b_list[j] = False
        return len([b for b in b_list if b])

    def countPrimes3(self, n: int) -> int:
        b_list = [False] * 2 + [True] * (n - 2)
        for i in range(2, int(math.sqrt(n)) + 1):
            if b_list[i]:
                b_list[i * i: n: i] = [False] * len(b_list[i * i: n: i])
        return sum(b_list)

    def countPrimes4(self, n: int) -> int:
        b_list = [False] * 2 + [True] * (n - 2)
        for i in range(2, int(math.sqrt(n)) + 1):
            if b_list[i]:
                b_list[i * i: n: i] = [False] * math.ceil((n - i * i) / i)
        return sum(b_list)


@pytest.fixture(scope="module")
def test_data():
    params_list = [
        (10,),
        (2,),
        (499979,),
    ]
    res_list = [
        4,
        0,
        41537,
    ]
    return params_list, res_list, 10


# def test_204(test_data):
#     func_test(Solution().countPrimes, *test_data)


def test_204_2(test_data):
    func_test(Solution().countPrimes2, *test_data)


def test_204_3(test_data):
    func_test(Solution().countPrimes3, *test_data)


def test_204_4(test_data):
    func_test(Solution().countPrimes4, *test_data)


if __name__ == '__main__':
    pytest.main(['-vv', '--durations=10', '-q', '--tb=line', '-x', '204 Count Primes.py'])
    # pytest.main(['-vv', '-x','204 Count Primes.py'])

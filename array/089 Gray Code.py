#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/16 10:13
# @File    : 089 Gray Code.py
# @Software: PyCharm

import pytest
from typing import List

from commons import func_test


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        t = 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(res[j] + t)
            t <<= 1
        return res

    def grayCode2(self, n: int) -> List[int]:
        res = [0]
        t = 1
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(t | res[j])
            t <<= 1
        return res

    def grayCode3(self, n: int) -> List[int]:
        res = [0] * 2 ** n
        t = 1
        for i in range(n):
            j = t - 1
            k = t
            while j >= 0:
                res[k] = res[j] + t
                j -= 1
                k += 1
            t <<= 1
        return res


@pytest.fixture(scope="module")
def test_data():
    params_list = [
    ]
    res_list = [
    ]
    for i in range(15):
        params_list.append((i,))
        res_list.append(Solution().grayCode(i))

    return params_list, res_list, 100


def test_89(test_data):
    func_test(Solution().grayCode, *test_data)


def test_89_2(test_data):
    func_test(Solution().grayCode2, *test_data)


def test_89_3(test_data):
    func_test(Solution().grayCode3, *test_data)


if __name__ == '__main__':
    pytest.main(['-vv', '--durations=10', '-q', '--tb=line', '-x', '089 Gray Code.py'])
    # print(Solution().grayCode(3))
    # for i in range(5):
    #     print(Solution().grayCode2(i))

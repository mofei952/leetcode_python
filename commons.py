#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/3/23 21:32
# @File    : commons.py
# @Software: PyCharm

import time
from functools import wraps
from typing import List


def func_test(func: callable, params_list: List, res_list: List, times: int = 1, after_func: callable = None):
    if len(params_list) != len(res_list):
        raise Exception('params count must equal to result count')
    for i in range(times):
        for j, params in enumerate(params_list):
            predict_res = res_list[j]
            res = func(*params)
            if after_func:
                res = after_func(res)
            assert res == predict_res, 'func:{}, param:{}, result:{}, predict:{}'.format(func.__name__, params, res,
                                                                                         predict_res)


def running_time(func):
    """运行时间装饰器"""

    @wraps(func)
    def wrapper(*args):
        t1 = time.perf_counter()
        result = func(*args)
        t2 = time.perf_counter()
        print(func.__name__, t2 - t1, sep='\t')
        return result

    return wrapper

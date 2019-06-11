#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2019/6/8 22:22
# @File    : 072 Edit Distance.py
# @Software: PyCharm

"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
You have the following 3 operations permitted on a word:
Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""

import heapq

import pytest

from commons import func_test


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if not n:
            return m
        if not m:
            return n
        dp = [[0 for j in range(m + 1)] for i in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = i
        for j in range(m + 1):
            dp[0][j] = j
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                t = 0 if word1[i - 1] == word2[j - 1] else 1
                dp[i][j] = min(dp[i - 1][j - 1] + t, dp[i][j - 1] + 1, dp[i - 1][j] + 1)
        return dp[-1][-1]

    def minDistance2(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if not n:
            return m
        if not m:
            return n
        dp = [i for i in range(m + 1)]
        dp2 = [0] * (m + 1)
        for i in range(1, n + 1):
            dp2[0] = i
            for j in range(1, m + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp2[j] = dp[j - 1]
                else:
                    dp2[j] = min(dp[j - 1], dp2[j - 1], dp[j]) + 1
            dp, dp2 = dp2, dp
        return dp[-1]

    def minDistance3(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        if word1 == word2:
            return 0
        if not n:
            return m
        if not m:
            return n
        dp = [i for i in range(m + 1)]
        for i in range(1, n + 1):
            pre = dp[0]
            dp[0] = i
            for j in range(1, m + 1):
                temp = dp[j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = pre
                else:
                    dp[j] = min(pre, dp[j - 1], dp[j]) + 1
                pre = temp
        return dp[-1]

    def minDistance4(self, word1, word2):
        seen = set()
        min_distance = max(len(word1), len(word2))

        def recursive(w1, w2, d):
            nonlocal min_distance
            if d > min_distance:
                return
            if (w1, w2, d) in seen:
                return
            seen.add((w1, w2, d))
            if not w1:
                min_distance = min(d + len(w2), min_distance)
                return
            if not w2:
                min_distance = min(d + len(w1), min_distance)
                return
            if w1 == w2:
                min_distance = min(d, min_distance)
                return
            while w1 and w2 and w1[-1] == w2[-1]:
                w1 = w1[:-1]
                w2 = w2[:-1]
            recursive(w1[:-1], w2[:-1], d + 1)
            recursive(w1, w2[:-1], d + 1)
            recursive(w1[:-1], w2, d + 1)

        recursive(word1, word2, 0)
        return min_distance

    def minDistance5(self, word1, word2):
        seen = set()
        queue = [(0, word1, word2)]
        while queue:
            min_item, min_index = queue[0], 0
            for i in range(1, len(queue)):
                if queue[i] < min_item:
                    min_item = queue[i]
                    min_index = i
            distance, w1, w2 = queue.pop(min_index)
            if w1 == w2:
                return distance
            if (w1, w2) not in seen:
                seen.add((w1, w2))
                while w1 and w2 and w1[-1] == w2[-1]:
                    w1 = w1[:-1]
                    w2 = w2[:-1]
                queue.append((distance + 1, w1, w2[:-1]))
                queue.append((distance + 1, w1[:-1], w2))
                queue.append((distance + 1, w1[:-1], w2[:-1]))

    def minDistance6(self, word1, word2):
        seen = set()
        heap = [(0, word1, word2)]
        while heap:
            distance, w1, w2 = heapq.heappop(heap)
            if w1 == w2:
                return distance
            if (w1, w2) not in seen:
                seen.add((w1, w2))
                while w1 and w2 and w1[-1] == w2[-1]:
                    w1 = w1[:-1]
                    w2 = w2[:-1]
                heapq.heappush(heap, (distance + 1, w1, w2[:-1]))
                heapq.heappush(heap, (distance + 1, w1[:-1], w2))
                heapq.heappush(heap, (distance + 1, w1[:-1], w2[:-1]))


@pytest.fixture(scope="module")
def test_data():
    params_list = [
        ('horse', 'ros'),
        ('intention', 'execution'),
        ('', ''),
        ('a', 'b'),
        ('abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy'),
        # ('pneumonoultramicroscopicsilicovolcanoconiosis', 'ultramicroscopically'),
    ]
    res_list = [
    ]
    for i in params_list:
        r = Solution().minDistance(*i)
        res_list.append(r)
    return params_list, res_list, 1000


def test_72(test_data):
    func_test(Solution().minDistance, *test_data)


def test_72_2(test_data):
    func_test(Solution().minDistance2, *test_data)


def test_72_3(test_data):
    func_test(Solution().minDistance3, *test_data)


def test_72_4(test_data):
    func_test(Solution().minDistance4, *test_data)


def test_72_5(test_data):
    func_test(Solution().minDistance5, *test_data)


def test_72_6(test_data):
    func_test(Solution().minDistance6, *test_data)


if __name__ == '__main__':
    pytest.main(['-vv', '--durations=10', '-q', '--tb=line', '-x', '072 Edit Distance.py'])

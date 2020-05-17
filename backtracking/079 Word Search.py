#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author  : mofei
# @Time    : 2020/5/12 20:25
# @File    : 079 Word Search.py
# @Software: PyCharm

"""
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

from collections import defaultdict
from copy import deepcopy
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if not m:
            return False

        n = len(board[0])
        if not n:
            return False

        board_count = defaultdict(int)
        word_count = defaultdict(int)
        for row in board:
            for s in row:
                board_count[s] += 1
        for s in word:
            word_count[s] += 1
        if any(c > board_count[s] for s, c in word_count.items()):
            return False

        def find_word(row, col, word_idx):
            # print(board, row, col, word[word_idx:])

            if word_idx == len(word) - 1:
                return True

            t = word[word_idx]
            board[row][col] = '$'

            if row > 0 and board[row - 1][col] == word[word_idx + 1] and find_word(row - 1, col, word_idx + 1):
                return True
            if col > 0 and board[row][col - 1] == word[word_idx + 1] and find_word(row, col - 1, word_idx + 1):
                return True
            if row < len(board) - 1 and board[row + 1][col] == word[word_idx + 1] and find_word(row + 1, col, word_idx + 1):
                return True
            if col < len(board[0]) - 1 and board[row][col + 1] == word[word_idx + 1] and find_word(row, col + 1, word_idx + 1):
                return True

            board[row][col] = t
            return False

        for i, row in enumerate(board):
            for j, s in enumerate(row):
                if s == word[0] and find_word(i, j, 0):
                    return True
        return False


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    print(Solution().exist(deepcopy(board), 'ABCCED'))
    print(Solution().exist(deepcopy(board), 'SEE'))
    print(Solution().exist(deepcopy(board), 'ABCB'))

    board = [
        ["C", "A", "A"],
        ["A", "A", "A"],
        ["B", "C", "D"]
    ]
    print(Solution().exist(board, 'AAB'))

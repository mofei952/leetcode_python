"""
https://leetcode.cn/problems/draw-line-lcci/
"""
from typing import List


class Solution:
    def drawLine(self, length: int, w: int, x1: int, x2: int, y: int) -> List[int]:
        row_nums = w // 32
        index1 = x1 // 32 + y * row_nums
        index2 = x2 // 32 + y * row_nums

        res = [0 for _ in range(index1)]

        for i in range(index1, index2 + 1):
            if index1 < i < index2:
                res.append(-1)
                continue

            negative = False
            bit_index1 = x1 % 32 if i == index1 else 0
            if bit_index1 == 0:
                negative = True
                bit_index1 = 1
            num = 2 ** (32 - bit_index1) - 1

            if i == index2:
                bit_index2 = x2 % 32
                num -= 2 ** (32 - bit_index2 - 1) - 1

            if negative:
                num = -(2 ** 31 - num)

            res.append(num)

        for _ in range(index2 + 1, length):
            res.append(0)

        print(res)
        return res


if __name__ == '__main__':
    Solution().drawLine(1, 32, 30, 31, 0)
    Solution().drawLine(3, 96, 0, 95, 0)
    Solution().drawLine(15, 96, 81, 95, 1)
    Solution().drawLine(24, 96, 2, 19, 5)
    Solution().drawLine(2, 64, 0, 52, 0)

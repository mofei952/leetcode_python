"""
https://leetcode.cn/problems/draw-line-lcci/
"""
from typing import List
import ctypes


class Solution:
    def drawLine(self, length: int, w: int, x1: int, x2: int, y: int) -> List[int]:
        cols = w // 32
        start = y * cols + x1 // 32
        end = y * cols + x2 // 32
        res = [0] * length

        for i in range(start + 1, end):
            res[i] = -1

        res[start] = 0xffffffff >> x1 % 32
        temp_end = (0xffffffff << (31 - x2 % 32)) & 0xffffffff
        res[end] = temp_end & res[start] if start == end else temp_end

        for i in [start, end]:
            if res[i] & 0x80000000 == 0x80000000:
                res[i] = -((res[i] ^ 0xffffffff) + 1)

        print(res)
        return res


if __name__ == '__main__':
    assert Solution().drawLine(1, 32, 30, 31, 0) == [3]
    assert Solution().drawLine(3, 96, 0, 95, 0) == [-1, -1, -1]
    assert Solution().drawLine(15, 96, 81, 95, 1) == [0, 0, 0, 0, 0, 32767, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert Solution().drawLine(24, 96, 2, 19, 5) == [
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        0, 0, 0, 1073737728, 0, 0, 0, 0, 0, 0, 0, 0]
    assert Solution().drawLine(2, 64, 0, 52, 0) == [-1, -2048]

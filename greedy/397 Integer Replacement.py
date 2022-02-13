"""
question:
https://leetcode.com/problems/integer-replacement/
"""


class Solution:
    def integerReplacement(self, n: int) -> int:
        step = 0
        while n != 1:
            if n & 1 == 0:
                n >>= 1
            elif n == 3 or n >> 1 & 1 == 0:
                n -= 1
            else:
                n += 1
            step += 1
        return step


if __name__ == '__main__':
    assert Solution().integerReplacement(9) == 4
    assert Solution().integerReplacement(8) == 3
    assert Solution().integerReplacement(7) == 4
    assert Solution().integerReplacement(3) == 2
    assert Solution().integerReplacement(65535) == 17
    assert Solution().integerReplacement(2 ** 31 - 1) == 32

"""
question:
https://leetcode.com/problems/patching-array/
"""
from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        combs = {0}
        for num in nums:
            combs |= {t + num for t in combs if t + num <= n}

        count = 0
        for i in range(31):
            num = 2 ** i
            if len(combs) > n:
                print(count)
                return count

            if num in combs:
                continue

            combs |= {t + num for t in combs if t + num <= n}
            count += 1


if __name__ == '__main__':
    Solution().minPatches([1, 3], 6)
    Solution().minPatches([1, 5, 10], 20)
    Solution().minPatches([1, 2, 2], 5)
    Solution().minPatches([1, 2, 31, 33], 2147483647)

"""
question:
https://leetcode.com/problems/remove-k-digits/
"""
from collections import defaultdict


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return '0'

        nums = [int(n) for n in num]

        num_counts = [0] * 10
        j = k + 1
        for i in range(j):
            num_counts[nums[i]] += 1
        # print(num_counts)

        res = []
        for i in range(len(nums)):
            n = nums[i]
            remove = False
            if i != j - 1:
                for jj in range(n - 1, -1, -1):
                    if num_counts[jj]:
                        remove = True
                        break
            if not remove:
                res.append(n)
                if j < len(nums):
                    num_counts[nums[j]] += 1
                    j += 1
            num_counts[n] -= 1

            # print(n, remove, num_counts, res)
            if len(res) == len(nums)-k:
                break

        return str(int(''.join(map(str, res))))


if __name__ == '__main__':
    assert Solution().removeKdigits('1432219', 3) == '1219'
    assert Solution().removeKdigits('10200', 1) == '200'
    assert Solution().removeKdigits('10', 2) == '0'
    assert Solution().removeKdigits('112', 1) == '11'

"""
question:
https://leetcode.com/problems/find-the-middle-index-in-array/
"""
from typing import List


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre_sum = 0
        post_sum = sum(nums)
        for i, num in enumerate(nums):
            post_sum -= num
            if pre_sum == post_sum:
                return i
            pre_sum += num
        return -1

    def findMiddleIndex2(self, nums: List[int]) -> int:
        # 提前计算累加的和，减少后面的计算
        # 实际效果没有比上面的解法效率高，可能是因为花费了更多时间来分配空间和赋值
        sums = [0]
        for i in range(len(nums)):
            sums.append(sums[i] + nums[i])
        total_sum = sums[-1]
        for i in range(len(nums)):
            if sums[i] == total_sum - sums[i + 1]:
                return i
        return -1


if __name__ == '__main__':
    assert Solution().findMiddleIndex2([2, 3, -1, 8, 4]) == 3
    assert Solution().findMiddleIndex2([1, -1, 4]) == 2
    assert Solution().findMiddleIndex2([2, 5]) == -1
    assert Solution().findMiddleIndex2([2]) == 0

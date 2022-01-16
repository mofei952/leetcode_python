"""
question:
https://leetcode.com/problems/gas-station/
"""
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start, end = len(gas) - 1, 0
        s = gas[start] - cost[start]
        while start > end:
            if s >= 0:
                s += gas[end] - cost[end]
                end += 1
            else:
                start -= 1
                s += gas[start] - cost[start]

        return start if s >= 0 else -1

    def canCompleteCircuit2(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        s = 0
        start = 0
        for i in range(len(gas)):
            s += gas[i] - cost[i]
            if s < 0:
                start = i + 1
                s = 0

        return start


if __name__ == '__main__':
    assert Solution().canCompleteCircuit2([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert Solution().canCompleteCircuit2([2, 3, 4], [3, 4, 3]) == -1
    assert Solution().canCompleteCircuit2([3], [3]) == 0
    assert Solution().canCompleteCircuit2([1], [3]) == -1

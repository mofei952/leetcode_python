"""
question:
https://leetcode.com/problems/gas-station/
"""
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, end = len(gas) - 1, 0
        sum = gas[start] - cost[start]
        while start > end:
            if sum >= 0:
                sum += gas[end] - cost[end]
                end += 1
            else:
                start -= 1
                sum += gas[start] - cost[start]
        return start if sum >= 0 else -1


if __name__ == '__main__':
    assert Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
    assert Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1
    assert Solution().canCompleteCircuit([3], [3]) == 0
    assert Solution().canCompleteCircuit([1], [3]) == -1

"""
question:
https://leetcode.com/problems/queue-reconstruction-by-height/
"""
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        hk = defaultdict(list)
        for h, k in people:
            hk[h].append(k)
        queue = []
        for h in sorted(hk.keys(), reverse=True):
            for k in sorted(hk[h]):
                queue.insert(k, [h, k])
        return queue


if __name__ == '__main__':
    assert Solution().reconstructQueue(
        [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    ) == [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
    assert Solution().reconstructQueue([]) == []
    assert Solution().reconstructQueue([[7, 0]]) == [[7, 0]]

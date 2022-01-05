"""
question:
https://leetcode.com/problems/queue-reconstruction-by-height/
"""
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        queue = []
        for h, k in sorted(people, key=lambda p: (-p[0], p[1])):
            queue.insert(k, (h, k))
        return queue


if __name__ == '__main__':
    assert Solution().reconstructQueue(
        [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    ) == [(5, 0), (7, 0), (5, 2), (6, 1), (4, 4), (7, 1)]
    assert Solution().reconstructQueue([]) == []
    assert Solution().reconstructQueue([[7, 0]]) == [(7, 0)]

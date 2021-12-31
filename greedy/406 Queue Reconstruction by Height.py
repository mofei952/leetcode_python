"""
question:
https://leetcode.com/problems/queue-reconstruction-by-height/
"""
import heapq
from collections import defaultdict
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        count_and_peoples = defaultdict(list)
        for h, k in people:
            heapq.heappush(count_and_peoples[k], h)
        queue = []
        for i in range(len(people)):
            for j in range(i, -1, -1):
                if count_and_peoples[j]:
                    h = heapq.heappop(count_and_peoples[j])
                    jj = sum(hh >= h for hh, kk in queue)
                    if jj == j:
                        queue.append([h, j])
                        break
                    else:
                        heapq.heappush(count_and_peoples[j], h)
        return queue


if __name__ == '__main__':
    assert Solution().reconstructQueue(
        [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    ) == [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]
    assert Solution().reconstructQueue([]) == []
    assert Solution().reconstructQueue([[7, 0]]) == [[7, 0]]

"""
question:
https://leetcode.com/problems/course-schedule/
"""
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for a, b in prerequisites:
            g[b].append(a)
            indegree[a] += 1

        queue = [i for i, indeg in enumerate(indegree) if indeg == 0]
        num = 0
        while queue:
            i = queue.pop(0)
            num += 1
            for j in g[i]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    queue.append(j)

        print(num == numCourses)
        return num == numCourses


if __name__ == '__main__':
    Solution().canFinish(2, [[1, 0]])
    Solution().canFinish(2, [[1, 0], [0, 1]])
    Solution().canFinish(3, [[1, 0], [0, 1], [1, 2]])
    Solution().canFinish(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    Solution().canFinish(1, [])

"""
question:
https://leetcode.cn/problems/robot-in-a-grid-lcci/
"""
from typing import List


class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return []

        path = []
        end = False
        visited = [[0] * n for _ in range(m)]

        def dfs(row, col):
            nonlocal end
            if visited[row][col] == 1 or obstacleGrid[row][col] == 1:
                return
            visited[row][col] = 1
            path.append([row, col])
            if row == m - 1 and col == n - 1:
                end = True
                return
            if row + 1 < m:
                dfs(row + 1, col)
                if end:
                    return
            if col + 1 < n:
                dfs(row, col + 1)
                if end:
                    return
            path.pop()

        dfs(0, 0)
        # print(path)
        return path

    def pathWithObstacles2(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return []

        path = []

        def dfs(row, col):
            if obstacleGrid[row][col] == 1:
                return
            obstacleGrid[row][col] = 1
            path.append([row, col])
            if row == m - 1 and col == n - 1:
                return True
            if row + 1 < m and dfs(row + 1, col):
                return True
            if col + 1 < n and dfs(row, col + 1):
                return True
            path.pop()

        dfs(0, 0)
        # print(path)
        return path

    def pathWithObstacles3(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return []

        dp = [[-1] * n for _ in range(m)]
        dp[0][0] = 0

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    continue
                if i > 0 and dp[i - 1][j] != -1:
                    dp[i][j] = (i - 1) * n + j
                elif j > 0 and dp[i][j - 1] != -1:
                    dp[i][j] = i * n + j - 1

        i, j = m - 1, n - 1
        if dp[i][j] == -1:
            return []
        path = [[i, j]]
        while i != 0 or j != 0:
            i, j = dp[i][j] // n, dp[i][j] % n
            path.append([i, j])

        # print(path[::-1])
        return path[::-1]


if __name__ == '__main__':
    assert Solution().pathWithObstacles3([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]) == [[0, 0], [0, 1], [0, 2], [1, 2], [2, 2]]
    assert Solution().pathWithObstacles3([[1]]) == []
    assert Solution().pathWithObstacles3([[0]]) == [[0, 0]]
    assert Solution().pathWithObstacles3([[0, 0], [1, 0]]) == [[0, 0], [0, 1], [1, 1]]

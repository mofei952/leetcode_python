"""
Given a m * n matrix mat and an integer K,
return a matrix answer where each answer[i][j] is the sum of
all elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K, and (r, c) is a valid position in the matrix.
 
Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]

Example 2:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n, K <= 100
1 <= mat[i][j] <= 100
"""

from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        arr = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                arr[i+1][j+1] = mat[i][j] + arr[i][j+1] + arr[i+1][j] - arr[i][j]

        dp = [[0] * (n) for _ in range(m)]
        for i in range(m):
            for j in range(n):
                r1, c1, r2, c2 = max(i-K, 0), max(j-K, 0), min(i+K+1, m), min(j+K+1, n)
                dp[i][j] = arr[r2][c2] - arr[r1][c2] - arr[r2][c1] + arr[r1][c1]

        return dp


def test1():
    res = Solution().matrixBlockSum(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1
    )
    assert res == [[12, 21, 16], [27, 45, 33], [24, 39, 28]]


def test2():
    res = Solution().matrixBlockSum(
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2
    )
    assert res == [[45, 45, 45], [45, 45, 45], [45, 45, 45]]

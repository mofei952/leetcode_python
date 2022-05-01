"""
question:
https://leetcode.com/problems/diagonal-traverse/
"""
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        res = []
        direct = 1
        i = j = 0
        while len(res) < n * m:
            if i < n and j < m:
                res.append(mat[i][j])
            if direct == 1:
                i -= 1
                j += 1
                if i < 0 or j >= m:
                    i += 1
                    direct = -1
            else:
                i += 1
                j -= 1
                if i >= n or j < 0:
                    j += 1
                    direct = 1
        return res


if __name__ == '__main__':
    Solution().findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    Solution().findDiagonalOrder([[1, 2], [3, 4]])

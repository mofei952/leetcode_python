"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 3
Output: [1,3,3,1]
"""

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        for i in range(rowIndex):
            temp_row = [1]
            for j in range(i):
                temp_row.append(row[j] + row[j+1])
            temp_row.append(1)
            row = temp_row
        return row

if __name__ == "__main__":
    row = Solution().getRow(3)
    print(row)
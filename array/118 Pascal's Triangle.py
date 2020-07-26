""" 
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []

        result = [[1]]    
        for i in range(numRows-1):
            row = [1]
            for j in range(i):
                row.append(result[-1][j] + result[-1][j + 1])
            row.append(1)
            result.append(row)
                
        return result
    
if __name__ == "__main__":
    result = Solution().generate(5)
    for row in result:
        print(row)
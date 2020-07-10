"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.

Example:
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = {()}
        for num in nums:
            result.update([subset + (num,) for subset in result])
        return list(result)


if __name__ == '__main__':
    res = Solution().subsetsWithDup([4, 4, 4, 1, 4])
    print(res)

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
        def dfs(index, temp_list):
            if index == len(nums):
                result.add(tuple(temp_list))
                return
            dfs(index + 1, temp_list)
            dfs(index + 1, temp_list + (nums[index], ))

        nums.sort()
        result = set()
        dfs(0, ())
        return result

    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = {()}
        for num in nums:
            result.update([subset + (num,) for subset in result])
        return list(result)

    def subsetsWithDup3(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]
        indexes = [-1]
        for i in range(len(nums)):
            for j in range(len(result)):
                if i > 0 and nums[i] == nums[i-1] and indexes[j] != i - 1:
                    continue
                result.append(result[j] + [nums[i]])
                indexes.append(i)
        return result


if __name__ == '__main__':
    res = Solution().subsetsWithDup3([4, 4, 4, 1, 4])
    print(res)

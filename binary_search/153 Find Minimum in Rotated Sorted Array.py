"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
You may assume no duplicate exists in the array.

Example 1:
Input: [3,4,5,1,2]
Output: 1

Example 2:
Input: [4,5,6,7,0,1,2]
Output: 0
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] < nums[-1]:
                high = mid - 1
            else:
                low = mid + 1
        return nums[low]


if __name__ == "__main__":
    assert Solution().findMin([2, 1]) == 1
    assert Solution().findMin([1, 2]) == 1
    assert Solution().findMin([3, 1, 2]) == 1
    assert Solution().findMin([3, 4, 5, 1, 2]) == 1
    assert Solution().findMin([4, 5, 6, 7, 0, 1, 2]) == 0

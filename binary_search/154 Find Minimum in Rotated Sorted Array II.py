"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
Find the minimum element.
The array may contain duplicates.

Example 1:
Input: [1,3,5]
Output: 1

Example 2:
Input: [2,2,2,0,1]
Output: 0

Note:
This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
"""

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if mid >= 1:
                while mid < high and nums[mid] == nums[mid-1]:
                    mid += 1
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid] <= nums[high]:
                high = mid - 1
            else:
                low = mid + 1
        return nums[low]

    def findMin2(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == nums[high]:
                high -= 1
            elif nums[mid] < nums[high]:
                high = mid
            else:
                low = mid + 1
        return nums[low]


if __name__ == "__main__":
    print(Solution().findMin2([1, 3, 5]))
    print(Solution().findMin2([2, 2, 2, 0, 1]))
    print(Solution().findMin2([3, 3, 1, 3]))
    print(Solution().findMin2([3, 1, 3, 3, 3]))
    print(Solution().findMin2([1, 1, 1]))

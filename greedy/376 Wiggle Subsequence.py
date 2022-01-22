"""
question:
https://leetcode.com/problems/wiggle-subsequence/
"""
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        count = 1
        last_asc = None
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            asc = nums[i] > nums[i - 1]
            if asc != last_asc:
                count += 1
            last_asc = asc
        return count

    def wiggleMaxLength2(self, nums: List[int]) -> int:
        dedup_nums = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                dedup_nums.append(nums[i])

        if len(dedup_nums) <= 2:
            return len(dedup_nums)

        count = 1
        last_asc = dedup_nums[1] > dedup_nums[0]
        for i in range(2, len(dedup_nums)):
            asc = dedup_nums[i] > dedup_nums[i - 1]
            if asc != last_asc:
                count += 1
            last_asc = asc

        return count + 1


if __name__ == '__main__':
    assert Solution().wiggleMaxLength([1, 7, 4, 9, 2, 5]) == 6
    assert Solution().wiggleMaxLength([1, 4, 7, 2, 5]) == 4
    assert Solution().wiggleMaxLength([1, 7, 4, 5, 5]) == 4
    assert Solution().wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]) == 7
    assert Solution().wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 2
    assert Solution().wiggleMaxLength([1, 7]) == 2
    assert Solution().wiggleMaxLength([1]) == 1
    assert Solution().wiggleMaxLength([0, 0]) == 1
    assert Solution().wiggleMaxLength([3, 3, 3, 2, 5]) == 3

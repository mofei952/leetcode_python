"""
question:
https://leetcode.com/problems/patching-array/
"""
from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        # 如果[1,x]已经被覆盖，将一个小于等于x+1的数y放入数组，则[1,x+y]能被完全覆盖
        #                     将一个大于    x+1的数y放入数组，则[1,x+y]不能被完全覆盖
        edge = 0
        i = 0
        res = 0
        while edge < n:
            if i < len(nums) and nums[i] <= edge + 1:
                edge += nums[i]
                i += 1
            else:
                # print('add: ', edge + 1)
                edge = edge * 2 + 1
                res += 1
        print(res)
        return res


if __name__ == '__main__':
    assert Solution().minPatches([1, 3], 6) == 1
    assert Solution().minPatches([1, 5, 10], 20) == 2
    assert Solution().minPatches([1, 2, 2], 5) == 0
    assert Solution().minPatches([1, 2, 31, 33], 2147483647) == 28

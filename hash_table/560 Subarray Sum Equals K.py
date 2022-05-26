from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # time limit exceeded
        sums = [0]
        sum = 0
        for num in nums:
            sum += num
            sums.append(sum)

        count = 0
        for i in range(len(sums)):
            for j in range(i + 1, len(sums)):
                if sums[j] - sums[i] == k:
                    count += 1

        return count

    def subarraySum2(self, nums: List[int], k: int) -> int:
        sums = []
        map = {}
        sum = 0

        for num in nums:
            sum += num
            sums.append(sum)
            if sum not in map:
                map[sum] = 1
            else:
                map[sum] += 1

        count = map[k] if k in map else 0
        for i in range(len(sums)):
            map[sums[i]] -= 1
            if k + sums[i] in map:
                count += map[k + sums[i]]

        return count

    def subarraySum3(self, nums: List[int], k: int) -> int:
        map = {0: 1}
        sum = 0
        count = 0
        for num in nums:
            sum += num
            if sum - k in map:
                count += map[sum - k]
            if sum not in map:
                map[sum] = 1
            else:
                map[sum] += 1
        return count


if __name__ == '__main__':
    assert Solution().subarraySum3([1, 1, 1], 2) == 2
    assert Solution().subarraySum3([1, 2, 3], 3) == 2
    assert Solution().subarraySum3([1], 1) == 1
    assert Solution().subarraySum3([1], 2) == 0
    assert Solution().subarraySum3([-1, -1, 1], 0) == 1
    assert Solution().subarraySum3([1, -1, 0], 0) == 3

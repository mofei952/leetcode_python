"""
question:
https://leetcode.com/problems/candy/
"""
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1]
        for i in range(1, len(ratings)):
            candies.append(candies[i - 1] + 1 if ratings[i] > ratings[i - 1] else 1)
        # print(candies)
        for i in range(len(ratings) - 2, -1, -1):
            candy = candies[i + 1] + 1 if ratings[i] > ratings[i + 1] else 1
            candies[i] = max(candy, candies[i])
        print(candies, sum(candies))
        return sum(candies)

    def candy2(self, ratings: List[int]) -> int:
        up = 1
        down = 0
        peak = 1
        res = 1
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                up += 1
                down = 0
                res += up
                peak = up
            elif ratings[i] < ratings[i - 1]:
                down += 1
                up = 1
                res += down
                if down >= peak:
                    res += 1
            else:
                up = 1
                down = 0
                res += up
                peak = up
        return res


if __name__ == '__main__':
    assert Solution().candy2([1, 0, 2]) == 5
    assert Solution().candy2([1, 2, 2]) == 4
    assert Solution().candy2([1, 2, 3, 2]) == 7
    assert Solution().candy2([2, 3, 2, 1]) == 7
    assert Solution().candy2([2, 1, 0, 1]) == 8
    assert Solution().candy2([2, 0, 1, 2]) == 8
    assert Solution().candy2([1, 3, 2, 2, 1]) == 7

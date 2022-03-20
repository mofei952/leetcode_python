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


if __name__ == '__main__':
    assert Solution().candy([1, 0, 2]) == 5
    assert Solution().candy([1, 2, 2]) == 4
    assert Solution().candy([1, 2, 3, 2]) == 7
    assert Solution().candy([2, 3, 2, 1]) == 7
    assert Solution().candy([2, 1, 0, 1]) == 8
    assert Solution().candy([2, 0, 1, 2]) == 8

"""
You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.



Example 1:


Input: n = 3
Output: 5
Explanation: The five different ways are show above.
Example 2:

Input: n = 1
Output: 1


Constraints:

1 <= n <= 1000
"""


class Solution:
    def numTilings(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[:3] = 1, 1, 2
        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2] + 2*sum(dp[:i-2])) % (10**9+7)
        return dp[n]

    def numTilings2(self, n: int) -> int:
        a, b, c = 0, 0, 1
        for _ in range(1, n+1):
            a, b, c = a+b, c, (a*2+b+c) % (10**9+7)
        return c

    def numTilings3(self, n: int) -> int:
        MOD = 10**9+7
        a, b, c = 0, 1, 1
        for _ in range(2, n+1):
            a, b, c = b, c, (2*c % MOD+a) % MOD
        return c

    def numTilings4(self, n: int) -> int:
        MOD = 10**9+7
        dp = [0] * (n+1)
        dp[:3] = 1, 1, 2
        for i in range(3, n+1):
            dp[i] = (2 * dp[i-1] % MOD + dp[i-3]) % MOD
        return dp[n]


if __name__ == '__main__':
    from time import perf_counter as pc
    t = pc()
    for i in range(1001):
        Solution().numTilings4(i)
        # print(i, Solution().numTilings4(i))
    print(pc()-t)

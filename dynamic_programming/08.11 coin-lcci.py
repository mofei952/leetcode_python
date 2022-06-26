"""
question:
https://leetcode.cn/problems/coin-lcci/
"""


class Solution:
    def waysToChange(self, n: int) -> int:
        cache = {}

        def dfs(total, index):
            if (total, index) in cache:
                return cache[(total, index)]

            if total == 0:
                return 1
            coins = [25, 10, 5, 1]
            count = 0
            for i in range(index, len(coins)):
                coin = coins[i]
                if coin <= total:
                    count += dfs(total - coin, i)

            cache[(total, index)] = count
            return count

        count = dfs(n, 0)
        # print(count)
        return count % 1000000007

    def waysToChange2(self, n: int) -> int:
        dp = [[1] + [0] * n for _ in range(4)]

        coins = [25, 10, 5, 1]
        for i in range(4):
            coin = coins[i]
            if n < coin:
                continue
            for j in range(1, n + 1):
                dp[i][j] = (dp[i][j - coin] + dp[i - 1][j]) % 1000000007

        # for row in dp:
        #     print(row)
        # print()
        return dp[-1][-1]

    def waysToChange3(self, n: int) -> int:
        dp = [1] + [0] * n
        coins = [25, 10, 5, 1]

        for i in range(4):
            coin = coins[i]
            step = 5 if coin == 10 else coin
            for j in range(coin, n + 1, step):
                dp[j] = (dp[j - coin] + dp[j]) % 1000000007
            # print(dp)

        # print()
        return dp[-1]


if __name__ == '__main__':
    Solution().waysToChange3(0)
    Solution().waysToChange3(5)
    Solution().waysToChange3(10)
    Solution().waysToChange3(25)
    Solution().waysToChange3(30)
    Solution().waysToChange3(50)

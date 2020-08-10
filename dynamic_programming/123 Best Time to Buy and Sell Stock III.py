"""
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

from typing import List
import sys


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_frist = buy_second = sys.maxsize
        profit_first = profit_second = 0
        for i in range(0, len(prices)):
            profit_first = max(profit_first, prices[i] - buy_frist)
            profit_second = max(profit_second, prices[i] - buy_second)
            buy_frist = min(buy_frist, prices[i])
            buy_second = min(buy_second, prices[i] - profit_first)
        return profit_second

    def maxProfit2(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        
        min_price = float('inf')
        dp = [0] * n
        for i in range(n):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
            dp[i] = max_profit

        max_price = 0
        for i in range(n-1, 0, -1):
            if prices[i] > max_price:
                max_price = prices[i]
                continue
            curr_max = max_price - prices[i]
            if curr_max + dp[i - 1] > max_profit:
                max_profit = curr_max + dp[i - 1]

        return max_profit


if __name__ == "__main__":
    print(Solution().maxProfit2([3, 3, 5, 0, 0, 3, 1, 4]))
    print(Solution().maxProfit2([1, 2, 3, 4, 5]))
    print(Solution().maxProfit2([7, 6, 4, 3, 1]))
    print(Solution().maxProfit2([4,7,2,1,11]))

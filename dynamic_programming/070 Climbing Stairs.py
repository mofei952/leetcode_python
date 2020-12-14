"""
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1, 2]
        for i in range(2, n):
            arr.append(arr[i - 1] + arr[i - 2])
        return arr[n - 1]

    def climbStairs2(self, n):
        a, b = 1, 1
        for _ in range(1, n):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    print(Solution().climbStairs2(1))
    print(Solution().climbStairs2(2))
    print(Solution().climbStairs2(28))

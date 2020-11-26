import heapq

"""
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:
Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:  
1 is typically treated as an ugly number.
n does not exceed 1690.
"""


class Solution:
    def __init__(self):
        self.dp = None

    def nthUglyNumber(self, n: int) -> int:
        if self.dp:
            return self.dp[n-1]

        self.dp = dp = []
        heap = [1]
        num_set = set()

        for _ in range(1690):
            x = heapq.heappop(heap)
            dp.append(x)
            if 2*x not in num_set:
                heapq.heappush(heap, 2*x)
                num_set.add(2*x)
            if 3*x not in num_set:
                heapq.heappush(heap, 3*x)
                num_set.add(3*x)
            heapq.heappush(heap, 5*x)
            num_set.add(5*x)

        return dp[n-1]

    def nthUglyNumber2(self, n: int) -> int:
        dp = [1]
        i2 = i3 = i5 = 0
        
        for _ in range(n):
            x = min(dp[i2]*2, dp[i3]*3, dp[i5]*5)
            dp.append(x)
            if x == dp[i2]*2:
                i2 += 1
            if x == dp[i3]*3:
                i3 += 1
            if x == dp[i5]*5:
                i5 += 1
                
        return dp[-1]
    
    def nthUglyNumber3(self, n: int) -> int:
        if self.dp:
            return self.dp[n-1]
        
        self.dp = dp = [1]
        i2 = i3 = i5 = 0
        
        for _ in range(1689):
            x = min(dp[i2]*2, dp[i3]*3, dp[i5]*5)
            dp.append(x)
            if x == dp[i2]*2:
                i2 += 1
            if x == dp[i3]*3:
                i3 += 1
            if x == dp[i5]*5:
                i5 += 1
        
        return dp[n-1]


if __name__ == "__main__":
    import time
    t = time.time()
    s = Solution()
    for i in range(1, 1691):
        s.nthUglyNumber(i)
        # print(i, s.nthUglyNumber2(i))
    print(time.time() - t)
    
    t = time.time()
    s = Solution()
    for i in range(1, 1691):
        s.nthUglyNumber2(i)
        # print(i, s.nthUglyNumber2(i))
    print(time.time() - t)
    
    t = time.time()
    s = Solution()
    for i in range(1, 1691):
        s.nthUglyNumber3(i)
        # print(i, s.nthUglyNumber2(i))
    print(time.time() - t)

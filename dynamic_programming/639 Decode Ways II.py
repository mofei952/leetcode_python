from functools import lru_cache


class Solution:
    def __init__(self) -> None:
        self.ways = dict(
            **{'*': 9, '0': 0},
            **{str(i): 1 for i in range(1, 10)},

            **{'**': 15},

            **{f'*{i}': 2 for i in range(0, 7)},
            **{f'*{i}': 1 for i in range(7, 10)},

            **{'0*': 0, '1*': 9, '2*': 6},
            **{f'{i}*': 0 for i in range(3, 10)},

            **{f'0{i}': 0 for i in range(0, 10)},
            **{str(i): 1 for i in range(10, 27)},
            **{str(i): 0 for i in range(27, 100)}
        )
        # print(self.map)

    # @lru_cache(None)
    # def ways(self, s):
    #     if len(s) == 1:
    #         if s == '*':
    #             return 9
    #         elif s == '0':
    #             return 0
    #         else:
    #             return 1
    #     else:
    #         if s[:2] == '**':
    #             return 15
    #         elif '*' not in s[:2]:
    #             if 9 < int(s) < 27:
    #                 return 1
    #         elif s[0] == '*':
    #             return 2 if int(s[1]) < 7 else 1
    #         else:
    #             if s[0] == '1':
    #                 return 9
    #             elif s[0] == '2':
    #                 return 6
    #     return 0

    def numDecodings(self, s: str) -> int:
        dp = [1] * (len(s)+1)
        dp[1] = self.ways[s[0]]

        for i in range(2, len(s)+1):
            n1 = dp[i-1] * self.ways[s[i-1]]
            n2 = dp[i-2] * self.ways[s[i-2: i]]
            dp[i] = (n1+n2) % (10**9+7)

        return dp[-1]


if __name__ == '__main__':
    print(Solution().numDecodings('*'))
    print(Solution().numDecodings('1*'))
    print(Solution().numDecodings('2*'))
    print(Solution().numDecodings('**'))
    print(Solution().numDecodings('***'))
    print(Solution().numDecodings('*1*1*0'))
    print(Solution().numDecodings('104'))
    print(Solution().numDecodings('*********'))
    print(Solution().numDecodings('7*9*3*6*3*0*5*4*9*7*3*7*1*8*3*2*0*0*6*'))
    print(Solution().numDecodings('904'))

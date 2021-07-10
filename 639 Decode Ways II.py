from functools import lru_cache


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 1
        if len(s) == 1:
            return 9 if s == '*' else 1
        func = self.numDecodings
        n1 = func(s[:1]) * func(s[1:])
        n2 = 0
        if s[:2] == '**':
            n2 = 15
        elif '*' not in s[:2]:
            if 0 < int(s) < 27:
                n2 = 1
        elif s[0] == '*':
            n2 = 2 if int(s[1]) < 7 else 1
        else:
            if s[0] == '1':
                n2 = 9
            elif s[0] == '2':
                n2 = 6
        if len(s) > 2:
            n2 *= func(s[2:])
        return n1 + n2

    @lru_cache(None)
    def f(self, s):
        if len(s) == 1:
            if s == '*':
                return 9
            elif s == '0':
                return 0
            else:
                return 1
        else:
            if s[:2] == '**':
                return 15
            elif '*' not in s[:2]:
                if 9 < int(s) < 27:
                    return 1
            elif s[0] == '*':
                return 2 if int(s[1]) < 7 else 1
            else:
                if s[0] == '1':
                    return 9
                elif s[0] == '2':
                    return 6
        return 0

    @lru_cache(None)
    def numDecodings(self, s):
        if len(s) == 1:
            return self.f(s)
        elif len(s) == 2:
            return self.f(s[0]) * self.f(s[1]) + self.f(s)
        else:
            res = self.f(s[:1])*self.numDecodings(s[1:]) + self.f(s[:2])*self.numDecodings(s[2:])
            if res > 10**9+7:
                return res % (10**9+7)
            else:
                return res


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

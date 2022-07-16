"""
question:
https://leetcode.cn/problems/one-away-lcci/
"""


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        m, n = len(first), len(second)
        if abs(m - n) > 1:
            return False
        if m == n:
            i = flag = 0
            while i < m:
                if first[i] != second[i]:
                    if flag == 1:
                        return False
                    flag = 1
                i += 1
            return True
        if n == m + 1:
            first, second = second, first
        i = j = 0
        while i < m and j < n:
            if first[i] != second[j]:
                i += 1
                if i - j > 1:
                    return False
            else:
                i += 1
                j += 1
        return True

    def oneEditAway2(self, first: str, second: str) -> bool:
        m, n = len(first), len(second)
        if abs(m - n) > 1:
            return False
        if n == m + 1:
            first, second = second, first
        for i, (x, y) in enumerate(zip(first, second)):
            if x != y:
                return first[i + 1:] == second[i + 1:] if m == n else first[i + 1:] == second[i:]
        return True

    def oneEditAway3(self, first: str, second: str) -> bool:
        m, n = len(first), len(second)
        if abs(m - n) > 1:
            return False
        if n == m + 1:
            first, second = second, first
        i = j = 0
        while i < m and j < n:
            if first[i] != second[j]:
                i += 1
                if m == n:
                    j += 1
                break
            i += 1
            j += 1
        while i < m and j < n:
            if first[i] != second[j]:
                return False
            i += 1
            j += 1
        return True


if __name__ == '__main__':
    assert Solution().oneEditAway3('pale', 'ple') is True
    assert Solution().oneEditAway3('pales', 'pal') is False
    assert Solution().oneEditAway3('a', 'b') is True
    assert Solution().oneEditAway3('teacher', 'bleacher') is False

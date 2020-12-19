"""
Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.
A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

Example 1:
Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].

Example 2:
Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.

Example 3:
Input: n = 33
Output: 66045

Constraints:
1 <= n <= 50 
"""


class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [1] * 5
        for _ in range(1, n):
            for j in range(1, 5):
                dp[j] += dp[j-1]
        return sum(dp)

    def countVowelStrings2(self, n: int) -> int:
        a = e = i = o = u = 1
        for _ in range(1, n):
            a, e, i, o = a+e+i+o+u, e+i+o+u, i+o+u, o+u
            # o += u
            # i += o
            # e += i
            # a += e
        return a+e+i+o+u

    def countVowelStrings3(self, n: int) -> int:
        return (n+1)*(n+2)*(n+3)*(n+4)//24


if __name__ == "__main__":
    for n in range(1, 11):
        print(n, Solution().countVowelStrings3(n))

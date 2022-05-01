"""
question:
https://leetcode.com/problems/group-anagrams/
"""
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            letter_counts = [0] * 26
            for c in s:
                letter_counts[ord(c) - 97] += 1
            anagrams[tuple(letter_counts)].append(s)
        # print(list(anagrams.values()))
        return list(anagrams.values())

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            letter_counts = [0] * 26
            for c in s:
                letter_counts[ord(c) - 97] += 1
            k = ''.join(chr(97 + i) + str(count) for i, count in enumerate(letter_counts) if count)
            anagrams[k].append(s)
        # print(list(anagrams.values()))
        return list(anagrams.values())

    def groupAnagrams3(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            k = ''.join(sorted(s))
            anagrams[k].append(s)
        # print(list(anagrams.values()))
        return list(anagrams.values())


if __name__ == '__main__':
    assert Solution().groupAnagrams3(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
        ['eat', 'tea', 'ate'],
        ['tan', 'nat'],
        ['bat']
    ]
    assert Solution().groupAnagrams3([""]) == [['']]
    assert Solution().groupAnagrams3(["a"]) == [['a']]

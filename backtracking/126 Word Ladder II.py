"""
Given two words (beginWord and endWord), and a dictionary's word list, 
find all shortest transformation sequence(s) from beginWord to endWord, such that:
Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

from typing import List
from collections import defaultdict


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        words = set(wordList)
        if endWord not in wordList:
            return []
        
        graph = defaultdict(set)
        word_length = len(wordList[0])
        bq = {beginWord}
        eq = {endWord}
        end = False
        rev = False

        while bq and not end:
            temp = set()
            words -= bq
            for x in bq:
                for i in range(word_length):
                    first, second = x[:i], x[i+1:]
                    for c in 'qwertyuiopasdfghjklzxcvbnm':
                        y = first + c + second
                        if y in words:
                            temp.add(y)
                            graph[y].add(x) if rev else graph[x].add(y)
                            if y in eq:
                                end = True
            bq = temp
            if len(bq) > len(eq):
                bq, eq, rev = eq, bq, not rev

        def bt(x):
            if x == endWord:
                return [[x]]
            res = []
            for y in graph[x]:
                for rest in bt(y):
                    res.append([x] + rest)
            return res

        return bt(beginWord)


if __name__ == "__main__":
    print(Solution().findLadders("hit", "cog",
                                 ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(Solution().findLadders("hit", "cog",
                                 ["hot", "dot", "dog", "lot", "log"]))
    print(Solution().findLadders("qa", "sq",
                                 ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar", "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or", "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"]))

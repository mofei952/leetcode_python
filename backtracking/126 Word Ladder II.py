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
from collections import deque


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

        result = []
        arr = []

        def bt(x):
            arr.append(x)
            if x == endWord:
                result.append(list(arr))
            else:
                for y in graph[x]:
                    bt(y)
            arr.pop()
        bt(beginWord)

        return result

    def findLadders2(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_length = len(wordList[0])
        adjacency_list = defaultdict(list)
        for w in wordList:
            for i in range(word_length):
                key = w[:i] + '_' + w[i+1:]
                adjacency_list[key].append(w)

        result = []
        q = deque()
        q.append([beginWord])
        visited = {}
        while q:
            arr = q.popleft()
            x = arr[-1]

            if x == endWord:
                result.append(arr)
                continue

            for i in range(word_length):
                k = x[:i] + '_' + x[i+1:]
                for y in adjacency_list[k]:
                    if y not in visited or len(arr) <= visited[y]:
                        visited[y] = len(arr)
                        q.append(arr + [y])

        return result


if __name__ == "__main__":
    print(Solution().findLadders2("hit", "cog",
                                  ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(Solution().findLadders2("hit", "cog",
                                  ["hot", "dot", "dog", "lot", "log"]))
    print(Solution().findLadders2("qa", "sq",
                                  ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar", "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or", "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb", "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"]))

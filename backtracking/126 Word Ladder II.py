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


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        shortest_length = len(wordList)
        word_length = len(wordList[0])
        result = []

        cur_word = beginWord
        sequence = [cur_word]
        visited_set = {cur_word}

        def dfs():
            nonlocal shortest_length, cur_word
            cur_word = sequence[-1]

            # print('seq:', sequence)

            if cur_word == endWord:
                result.append(list(sequence))
                if len(sequence) < shortest_length:
                    shortest_length = len(sequence)
                return
            if len(sequence) >= shortest_length:
                return

            words = [
                w for w in wordList
                if w not in visited_set and sum(
                    [cur_word[i] != w[i] for i in range(word_length)]
                ) == 1
            ]

            # print('word:', words)

            for w in words:
                sequence.append(w)
                visited_set.add(w)
                dfs()
                sequence.pop()
                visited_set.remove(w)

        dfs()
        result = [seq for seq in result if len(seq) == shortest_length]
        return result


if __name__ == "__main__":
    print(Solution().findLadders("hit", "cog",
                                 ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(Solution().findLadders("hit", "cog",
                                 ["hot", "dot", "dog", "lot", "log"]))

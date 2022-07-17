"""
question:
https://leetcode.cn/problems/word-transformer-lcci/
"""
import string
from typing import List


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        # 超时
        cache = {}

        def match(w1, w2):
            if (w1, w2) in cache:
                return cache[(w1, w2)]

            diff_count = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    diff_count += 1
                    if diff_count > 1:
                        break
            is_match = diff_count == 1

            cache[(w1, w2)] = is_match
            return is_match

        res = [beginWord]
        visited_words = set()

        def dfs(word, words):
            if word in visited_words:
                return False
            visited_words.add(word)

            if word == endWord:
                return True

            for i, w in enumerate(words):
                if w in res:
                    continue
                if match(w, word):
                    res.append(w)
                    words.remove(w)
                    if dfs(w, words):
                        return True
                    words.insert(i, w)
                    res.pop()

        dfs(beginWord, wordList)

        if len(res) == 1:
            res = []
        print(res)
        return res

    def findLadders2(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        # dfs + 遍历字母快速获得编辑距离为1的有效单词 + 剪枝
        def dfs(word, words):
            if word == endWord:
                return True

            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    w = word[:i] + c + word[i + 1:]

                    if w not in words:
                        continue
                    words.remove(w)

                    res.append(w)
                    if dfs(w, words):
                        return True
                    res.pop()

        res = [beginWord]
        words = set(wordList)
        if beginWord in words:
            words.remove(beginWord)
        if dfs(beginWord, words):
            print(res)
            return res
        print([])
        return []

    def findLadders3(self, beginWord: str, endWord: str, wordList: List[str]) -> List[str]:
        # bfs + 遍历字母快速获得编辑距离为1的有效单词（没有算法2快）
        queue = [beginWord]
        words = set(wordList)
        previous_map = {}
        while queue:
            word = queue.pop()
            if word == endWord:
                break
            for i in range(len(word)):
                for c in string.ascii_lowercase:
                    w = word[:i] + c + word[i + 1:]
                    if w in words:
                        words.remove(w)
                        queue.append(w)
                        previous_map[w] = word
        else:
            print([])
            return []
        word = endWord
        res = [word]
        while word != beginWord:
            word = previous_map[word]
            res.append(word)
        print(res[::-1])
        return res[::-1]


if __name__ == '__main__':
    # dfs、bfs、记忆化搜索、剪枝、遍历字母快速获得编辑距离为1的有效单词
    Solution().findLadders2('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'])
    Solution().findLadders2('hit', 'cog', ["hot", "dot", "dog", "lot", "log"])
    Solution().findLadders2('hot', 'dog', ["hot", "dog", "dot"])
    Solution().findLadders2('a', 'c', ['a', "b", "c"])
    Solution().findLadders2(
        "qa", "sq", [
            "si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le", "av", "sm", "ar", "ci",
            "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn", "ya", "cr", "po", "fe", "ho", "ma", "re", "or",
            "rn", "au", "ur", "rh", "sr", "tc", "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb",
            "sh", "co", "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an", "me", "mo",
            "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io", "be", "fm", "ta", "tb", "ni", "mr",
            "pa", "he", "lr", "sq", "ye"
        ]
    )

    Solution().findLadders2(
        "cet",
        "ism",
        ["kid", "tag", "pup", "ail", "tun", "woo", "erg", "luz", "brr", "gay", "sip", "kay", "per", "val", "mes", "ohs",
         "now", "boa", "cet", "pal", "bar", "die", "war", "hay", "eco", "pub", "lob", "rue", "fry", "lit", "rex", "jan",
         "cot", "bid", "ali", "pay", "col", "gum", "ger", "row", "won", "dan", "rum", "fad", "tut", "sag", "yip", "sui",
         "ark", "has", "zip", "fez", "own", "ump", "dis", "ads", "max", "jaw", "out", "btu", "ana", "gap", "cry", "led",
         "abe", "box", "ore", "pig", "fie", "toy", "fat", "cal", "lie", "noh", "sew", "ono", "tam", "flu", "mgm", "ply",
         "awe", "pry", "tit", "tie", "yet", "too", "tax", "jim", "san", "pan", "map", "ski", "ova", "wed", "non", "wac",
         "nut", "why", "bye", "lye", "oct", "old", "fin", "feb", "chi", "sap", "owl", "log", "tod", "dot", "bow", "fob",
         "for", "joe", "ivy", "fan", "age", "fax", "hip", "jib", "mel", "hus", "sob", "ifs", "tab", "ara", "dab", "jag",
         "jar", "arm", "lot", "tom", "sax", "tex", "yum", "pei", "wen", "wry", "ire", "irk", "far", "mew", "wit", "doe",
         "gas", "rte", "ian", "pot", "ask", "wag", "hag", "amy", "nag", "ron", "soy", "gin", "don", "tug", "fay", "vic",
         "boo", "nam", "ave", "buy", "sop", "but", "orb", "fen", "paw", "his", "sub", "bob", "yea", "oft", "inn", "rod",
         "yam", "pew", "web", "hod", "hun", "gyp", "wei", "wis", "rob", "gad", "pie", "mon", "dog", "bib", "rub", "ere",
         "dig", "era", "cat", "fox", "bee", "mod", "day", "apr", "vie", "nev", "jam", "pam", "new", "aye", "ani", "and",
         "ibm", "yap", "can", "pyx", "tar", "kin", "fog", "hum", "pip", "cup", "dye", "lyx", "jog", "nun", "par", "wan",
         "fey", "bus", "oak", "bad", "ats", "set", "qom", "vat", "eat", "pus", "rev", "axe", "ion", "six", "ila", "lao",
         "mom", "mas", "pro", "few", "opt", "poe", "art", "ash", "oar", "cap", "lop", "may", "shy", "rid", "bat", "sum",
         "rim", "fee", "bmw", "sky", "maj", "hue", "thy", "ava", "rap", "den", "fla", "auk", "cox", "ibo", "hey", "saw",
         "vim", "sec", "ltd", "you", "its", "tat", "dew", "eva", "tog", "ram", "let", "see", "zit", "maw", "nix", "ate",
         "gig", "rep", "owe", "ind", "hog", "eve", "sam", "zoo", "any", "dow", "cod", "bed", "vet", "ham", "sis", "hex",
         "via", "fir", "nod", "mao", "aug", "mum", "hoe", "bah", "hal", "keg", "hew", "zed", "tow", "gog", "ass", "dem",
         "who", "bet", "gos", "son", "ear", "spy", "kit", "boy", "due", "sen", "oaf", "mix", "hep", "fur", "ada", "bin",
         "nil", "mia", "ewe", "hit", "fix", "sad", "rib", "eye", "hop", "haw", "wax", "mid", "tad", "ken", "wad", "rye",
         "pap", "bog", "gut", "ito", "woe", "our", "ado", "sin", "mad", "ray", "hon", "roy", "dip", "hen", "iva", "lug",
         "asp", "hui", "yak", "bay", "poi", "yep", "bun", "try", "lad", "elm", "nat", "wyo", "gym", "dug", "toe", "dee",
         "wig", "sly", "rip", "geo", "cog", "pas", "zen", "odd", "nan", "lay", "pod", "fit", "hem", "joy", "bum", "rio",
         "yon", "dec", "leg", "put", "sue", "dim", "pet", "yaw", "nub", "bit", "bur", "sid", "sun", "oil", "red", "doc",
         "moe", "caw", "eel", "dix", "cub", "end", "gem", "off", "yew", "hug", "pop", "tub", "sgt", "lid", "pun", "ton",
         "sol", "din", "yup", "jab", "pea", "bug", "gag", "mil", "jig", "hub", "low", "did", "tin", "get", "gte", "sox",
         "lei", "mig", "fig", "lon", "use", "ban", "flo", "nov", "jut", "bag", "mir", "sty", "lap", "two", "ins", "con",
         "ant", "net", "tux", "ode", "stu", "mug", "cad", "nap", "gun", "fop", "tot", "sow", "sal", "sic", "ted", "wot",
         "del", "imp", "cob", "way", "ann", "tan", "mci", "job", "wet", "ism", "err", "him", "all", "pad", "hah", "hie",
         "aim", "ike", "jed", "ego", "mac", "baa", "min", "com", "ill", "was", "cab", "ago", "ina", "big", "ilk", "gal",
         "tap", "duh", "ola", "ran", "lab", "top", "gob", "hot", "ora", "tia", "kip", "han", "met", "hut", "she", "sac",
         "fed", "goo", "tee", "ell", "not", "act", "gil", "rut", "ala", "ape", "rig", "cid", "god", "duo", "lin", "aid",
         "gel", "awl", "lag", "elf", "liz", "ref", "aha", "fib", "oho", "tho", "her", "nor", "ace", "adz", "fun", "ned",
         "coo", "win", "tao", "coy", "van", "man", "pit", "guy", "foe", "hid", "mai", "sup", "jay", "hob", "mow", "jot",
         "are", "pol", "arc", "lax", "aft", "alb", "len", "air", "pug", "pox", "vow", "got", "meg", "zoe", "amp", "ale",
         "bud", "gee", "pin", "dun", "pat", "ten", "mob"])

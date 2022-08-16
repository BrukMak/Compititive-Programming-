class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        wordSet = set()
        res = ""
        for word in words:
            if len(word) == 1 or  word[:-1] in wordSet:
                wordSet.add(word)
                if len(word) > len(res): res = word
        return res
        
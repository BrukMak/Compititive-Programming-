class Solution:
    def checkValid(self, word1, word2):
        ans = False
        for i in range(len(word2)):
            if word1 == word2[:i] + word2[i+1:]:
                ans = True
        return ans
            
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key = len)
        return self.continousSeq(0, words, None, {})
    def continousSeq(self, index, words, prev, memo):
        state = (index, prev)
        if state in memo:
            return memo[state]
        if index == len(words):
            return 0
        take = 0
        skip = 0
        if not prev or (len(words[index]) == 1 + len(prev) and self.checkValid(prev, words[index])):
            take = 1 + self.continousSeq(index + 1, words, words[index], memo)
        skip = self.continousSeq(index + 1, words, prev, memo)
        memo[state] = max(skip, take)
        return max(skip, take)
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        ans = word
        for i in range(len(word)):
            if word[i] == ch:
                rem = word[i+1:]
                toReverse = word[:i+1]
                toReverse = toReverse[::-1]
                ans = toReverse + rem
                break
        return ans
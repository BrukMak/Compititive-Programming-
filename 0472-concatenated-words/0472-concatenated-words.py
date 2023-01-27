class Solution:
    def concatenatedWord(self, word, words):
        
        for i in range(1, len(word)):
            prefix = word[:i]
            sufix = word[i:]
            if prefix in words and (sufix in words or self.concatenatedWord(sufix, words)):
                return True
        return False
        
        
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        
        """
        words = [cats, dog, catsdogcats, rat, ratcatscats]
        
        output = [catsdogcats, ratcatscats]

        """
        
        words = set(words)
        answer = []
        for word in words:
            if self.concatenatedWord(word, words):
                answer.append(word)
        return answer
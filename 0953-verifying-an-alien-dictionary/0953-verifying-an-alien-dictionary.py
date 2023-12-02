class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        n = len(words)
        
        def isValid(word1, word2):
            p1, p2 = 0, 0
            while p1 < len(word1) and p2 < len(word2) and word1[p1] == word2[p2]:
                p1 += 1
                p2 += 1
                
            if p1 < len(word1) and p2 < len(word2):
                i1 = order.index(word1[p1])
                i2 = order.index(word2[p2])
                return i1 < i2
            elif (p2 < len(word2) and p1 >= len(word1)) or  (p1 >= len(word1) and  p2 >= len(word2)) :
                return True
            else:
                return False
                
        for i in range(n-1):
            if not isValid(words[i], words[i+1]):
                return False
            
        return True
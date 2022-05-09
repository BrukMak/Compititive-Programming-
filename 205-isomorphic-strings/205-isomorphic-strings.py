class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        vocabulary = {}
        for ch1, ch2 in zip(s, t):
            if ch1 not in vocabulary:
                if ch2 in set(vocabulary.values()):
                    return False
                vocabulary[ch1] = ch2
                
            else:
                if ch2 != vocabulary[ch1]:
                    return False
        return True
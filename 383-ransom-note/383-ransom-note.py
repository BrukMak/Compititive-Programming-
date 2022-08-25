class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = defaultdict(int)
        c2 = defaultdict(int)
        
        for c in ransomNote:
            c1[c] += 1
        for c in magazine:
            c2[c] += 1
        
        for ch in c1.keys():
            
            if c1[ch] > c2[ch]:
                return False
            
        return True
        
        
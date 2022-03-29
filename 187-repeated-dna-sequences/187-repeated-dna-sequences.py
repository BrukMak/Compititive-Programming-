class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = []
        di = defaultdict(int)
        start = 0
        while start + 10 <= len(s):
            # print(s[start: start + 10])
            di[s[start: start + 10]] += 1
            
            start += 1
        for key,val in di.items():
            if val > 1:
                ans.append(key)
        return ans
                
        

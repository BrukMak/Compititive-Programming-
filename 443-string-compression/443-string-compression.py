class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        l, r = 0, 0
        while l < len(chars):
            if r < len(chars) and chars[l] == chars[r]:
                r += 1
            else:
                if r - l > 1 and r - l < 10:
                    s += chars[l]
                    s += str(r-l)
                    
                elif r - l > 1 and r - l >= 10:
                    s += chars[l]
                    c = str(r - l)
                    
                    for i in c:
                        s += i
                else:
                    s += chars[l]
                l = r
        
        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)   
                    
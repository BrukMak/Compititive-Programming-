class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        # Make sure the list gonna have atleast two elements
        return self.spliter(0, [], n, s)
    
    def spliter(self, index, cur, n, s):
        if index >= n and len(cur) > 1:
            return True
        if index >= n:
            return False
        
    
        for i in range(index+1, n+1):
            if not cur or cur[-1] - 1 == int(s[index:i]):
                cur.append(int(s[index:i]))
                if self.spliter(i, cur, n, s):
                    return True
                cur.pop()
                
        return False
            
            
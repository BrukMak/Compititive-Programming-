class Solution:
    def splitString(self, s: str) -> bool:
        n = len(s)
        # Make sure the list gonna have atleast two elements
        
        for i in range(1, n):
            if self.spliter(i, [int(s[:i])], n, s):
                return True
        return False
    
    def spliter(self, index, cur, n, s):
        if index >= n:
            return True
        for i in range(index+1, n+1):
            if cur[-1] - 1 == int(s[index:i]):
                cur.append(int(s[index:i]))
                if self.spliter(i, cur, n, s):
                    return True
                cur.pop()
                
        return False
            
            
class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []     
        star = []    
        
        for i in range(len(s)):
            if s[i] == "(":                 
                left.append(i)
            elif s[i] == "*":
                star.append(i)
            elif s[i] == ")":              
                if left:          
                    left.pop()
                elif star:            
                    star.pop()
                else:
                    return False           
        
        while left:               
            if star and star[-1] > left[-1]: 
                star.pop()
                left.pop()
            else:
                return False
            
        return True
        

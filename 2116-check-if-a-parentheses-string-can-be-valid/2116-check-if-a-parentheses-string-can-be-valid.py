class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        count = 0
        
        for c, l in zip(s, locked):
            if l == '0' or c == '(':
                count += 1
            else: count -= 1
                     
            if count < 0:
                return False
        count = 0
        for c, l in zip(reversed(s), reversed(locked)):
            if l == '0' or c == ')':
                count += 1
            else: count -= 1
                     
            if count < 0:
                return False
        return True
                
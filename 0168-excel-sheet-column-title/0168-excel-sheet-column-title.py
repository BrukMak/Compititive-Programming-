class Solution:
    def __init__(self):
        self.res = []
    def convertToTitle(self, columnNumber: int) -> str:
        if not columnNumber:
            return "".join(self.res[::-1]) 
                           
        rem = columnNumber % 26 
        if not rem: rem = 26
        self.res.append(chr(rem + 64))
        columnNumber -= rem
        columnNumber //= 26
        
        return self.convertToTitle(columnNumber)

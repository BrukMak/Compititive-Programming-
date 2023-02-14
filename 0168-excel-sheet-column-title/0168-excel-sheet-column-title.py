class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []

        while columnNumber:
            rem = columnNumber % 26 
            if not rem: rem = 26
            res.append(chr(rem + 64))
            columnNumber -= rem
            columnNumber //= 26
            
        return "".join(res[::-1])
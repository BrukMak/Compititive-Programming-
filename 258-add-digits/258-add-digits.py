class Solution:
    def addDigits(self, num: int) -> int:
        
        if num <= 9:
            return num
        else:
            numStr =  str(num)
            while len(numStr) > 1:
                
                cur = 0
                for i in range(len(numStr)):
                    cur += int(numStr[i])
                numStr = str(cur)
            return int(numStr)
        
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        res = 0
        corMinutes = int(correct[:2])*60 + int(correct[3:])  
        curMinutes=  int(current[:2]) * 60 +  int(current[3:])
        minutes = corMinutes - curMinutes
        while minutes > 0:
            if minutes >= 60:
                res += minutes // 60
                minutes -= (minutes // 60) * 60
            elif minutes >= 15:
                res += minutes // 15
                minutes -= (minutes // 15)* 15
            elif minutes >= 5:
                res += minutes // 5
                minutes -= (minutes // 5) * 5
            else:
                res += minutes
                minutes = 0
        return res
                

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        answer = []
        for hour in range(12):
            for minute in range(60):
                if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
                    res = str(hour) + ':' 
                    if not minute:
                        res += "00"
                    elif minute < 10:
                        res += "0" + str(minute)
                    else:
                        res += str(minute)
                    answer.append(res)
        return answer
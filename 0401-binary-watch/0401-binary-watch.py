class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn > 8:
            return []
        hours = [8, 4, 2, 1]
        minutes = [32, 16, 8, 4, 2, 1]
        answer = set()
        self.backTrack(turnedOn, 0, 0, answer, hours, minutes, set(), set())
        return sorted(list(answer))
    def backTrack(self, n, cur_hr, cur_min, answer, hours, minutes, vis_hr, vis_min):
        if n == 0:
            ans = ""
            if cur_hr < 12 and cur_min < 60:
                if not cur_hr:
                    ans += "0:"
                else:
                    ans += str(cur_hr) + ":"
                    
                if not cur_min:
                    ans += "00"
                elif cur_min < 10:
                    ans += "0" + str(cur_min)
                else:
                    ans += str(cur_min)
                answer.add(ans)
            return
        for hr in hours:
            if hr not in vis_hr:
                cur_hr += hr
                n -= 1
                vis_hr.add(hr)
                self.backTrack(n, cur_hr, cur_min, answer, hours, minutes, vis_hr, vis_min)
                vis_hr.remove(hr)
                n += 1
                cur_hr -= hr
        for m in minutes:
            if m not in vis_min:
                cur_min += m
                n -= 1
                vis_min.add(m)
                self.backTrack(n, cur_hr, cur_min, answer, hours, minutes, vis_hr, vis_min)
                vis_min.remove(m)
                n += 1
                cur_min -= m
        
            
            
        
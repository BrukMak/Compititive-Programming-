class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            cur = []
            ptr = 0
            while ptr < len(s):
                kpart = 0
                for idx in range(ptr, min(ptr+k,len(s))):
                    kpart += int(s[idx])
                
                cur.append(str(kpart))
                ptr += k
                
            s = "".join(cur)
            
        return s
class Solution:
    def maximumSwap(self, num: int) -> int:
        if num < 10:
            return num
        num = list(str(num))
        possible = None
        for i in range(len(num)):
        
            for j in range(len(num)-1, i, -1):
                if (not possible and num[j] > num[i]) or (possible and num[j] > num[possible]):
                    possible = j
                    
            if possible:
                num[possible] , num[i] = num[i], num[possible]
                return int("".join(num))
            
        return int("".join(num))
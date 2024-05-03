class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        v1 = [int(val) for val in v1]
        v2 = [int(val) for val in v2]
        
        if len(v1) < len(v2):
            v1 += [0]*(len(v2)-len(v1))
            
        if len(v2) < len(v1):
            v2 += [0]*(len(v1)-len(v2))
        
        for i in range(len(v1)):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        
        return 0
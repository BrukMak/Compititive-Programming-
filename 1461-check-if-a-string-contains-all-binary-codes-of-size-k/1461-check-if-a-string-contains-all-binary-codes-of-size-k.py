class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        allComb = set()
        for i in range(len(s)-(k-1)):
            allComb.add(s[i:i+k])
        if  2 ** k > len(allComb): return False
        return True
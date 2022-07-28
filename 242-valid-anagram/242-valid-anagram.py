class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCnt = Counter(s)
        tCnt = Counter(t)
        for key, val in sCnt.items():
            if tCnt[key] != val:
                return False
        return True
        
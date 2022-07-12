class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num += digits[-(i+1)] * 10**i
        
        num += 1
        num = str(num)
        ans = list(num.strip())
        return ans
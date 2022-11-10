class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ""
        for n in digits:
            num += str(n)
        
        num = int(num)
        num += 1
        num = [*str(num)]
        
        return num
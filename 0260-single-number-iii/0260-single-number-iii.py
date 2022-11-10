class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Find the xor of the whole list
        xor = 0
        for num in nums:
            xor ^= num
        # Find the first/any position the xor is 1
        # B/C is the xor is 1 that means one of them is 1 the other is zero at that position
        pos = self.findPos(xor)
        half1 = 0
        half2 = 0
        
        # Group the whole list in to two with the req being having 1 at the pos
        for num in nums:
            if num & 1 << pos:
                half1 ^= num
            else:
                half2 ^= num
                
                
        return [half1, half2]
    
    
    def findPos(self, xor):
        for i in range(32):
            test = xor & 1 << i
            if test:
                return i

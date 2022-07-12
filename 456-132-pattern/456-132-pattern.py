class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        dec = []
        minLeft = nums[0]
        for val in nums[1:]:
            while dec and dec[-1][0] <= val:
                dec.pop()
            if dec and dec[-1][1] < val:
                return True
            
            dec.append([val, minLeft])
            minLeft = min(minLeft, val)
        return False
            
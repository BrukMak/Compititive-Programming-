class Solution:
    def canJump(self, nums: List[int]) -> bool:
        final_pt = 0
        
        for idx, num in enumerate(nums):
            if final_pt < idx:
                return False
            
            final_pt = max(final_pt, num + idx)
            
        return True
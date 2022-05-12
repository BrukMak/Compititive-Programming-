class Solution:
    def numberOfSteps(self, num: int) -> int:
        step_count = 0
        
        while num > 0:
            if not num & 1:
                num = num >> 1
            else:
                num = num & (~1)
            step_count += 1
        return step_count
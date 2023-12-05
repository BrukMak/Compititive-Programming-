class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        inc_stack = []
        count = 0
        for num in nums:
            if len(inc_stack) > 1 and num < inc_stack[-2]:
                inc_stack.append(inc_stack[-1])
                count += 1
                if count > 1:
                    return False
                continue
                
            while inc_stack and num < inc_stack[-1]:
                inc_stack.pop()
                count += 1
                if count > 1:
                    return False
            inc_stack.append(num)
            
        return True
                
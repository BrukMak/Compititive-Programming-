class Solution:
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        nums = [i for i in range(1, n+1)]
        
        def backTracking(i, curr):
            if len(curr) == k:
                combinations.append(curr[:])
                return
            if i >= n:
                return
            
            curr.append(nums[i])
            backTracking(i+1, curr)
            curr.pop()
            backTracking(i+1, curr)
            
        backTracking(0, [])
        return combinations
                
        
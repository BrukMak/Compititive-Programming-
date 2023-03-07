class Solution:
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        nums = [i for i in range(1, n+1)]
        
        def backTracking(i, curr):
            if i >= n:
                if len(curr) == k:
                    ans.append(curr[:])
            
                return
            curr.append(nums[i])
            backTracking(i+1, curr)
            curr.pop()
            backTracking(i+1, curr)
            
        backTracking(0, [])
        return ans
                
        
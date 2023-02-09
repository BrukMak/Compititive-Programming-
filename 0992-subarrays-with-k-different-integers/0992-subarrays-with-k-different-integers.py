class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        
        
        def helper(K):
            result = 0
            count = defaultdict(int)
            r = 0
            l = 0
            while r < len(nums):
                count[nums[r]] += 1
                while len(count) > K:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        del count[nums[l]]
                    l += 1
                result += r - l + 1
                r += 1
                
            return result
        
        return helper(k) - helper(k - 1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        n_set = set(nums)
        
        for i in nums:
            count = 1
            if i - 1 in n_set:
                continue
            else:
                while i + 1 in n_set:
                    count += 1
                    i += 1
            ans = max(ans,count)
            
        return ans
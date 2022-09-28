class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        window, l = 0 , 0
        cnt = defaultdict(int)
        for r in range(len(nums)):
            if nums[r] == 0: cnt[0] += 1
            while cnt[0] > k:
                if nums[l] == 0:
                    cnt[0] -= 1
                l += 1
                
            window = max(window, r - l + 1)
        return window
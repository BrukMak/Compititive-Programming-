class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        prefix = 0
        prev_mod = defaultdict(int)
        prev_mod[0] = 1
        subarrays = 0
        for i in range(len(nums)):
            prefix += nums[i]
            mod = prefix % k
            if mod in prev_mod:
                subarrays += prev_mod[mod]
            prev_mod[mod] += 1
        
        return subarrays    
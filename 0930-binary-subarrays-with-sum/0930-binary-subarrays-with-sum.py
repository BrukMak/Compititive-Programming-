class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        sum_count = defaultdict(int)
        sum_count[0] = 1
        prefix_sum = 0
        subarray_count = 0
        
        for num in nums:
            prefix_sum += num
            target = prefix_sum - goal
            if target in sum_count:
                subarray_count += sum_count[target]
            sum_count[prefix_sum] += 1
            
        print(sum_count)
        return subarray_count
        
        
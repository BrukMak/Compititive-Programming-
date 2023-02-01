class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        prefix_sum = 0
        count = 0
        for num in nums:
            prefix_sum += num - prefix_sum
            count += 1 if num != 0 else 0
            if prefix_sum > nums[-1]:
                return count
            
        return count
    
    
    
    
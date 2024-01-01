class Solution:
    def check_divisibility(self, arr, k):
        accumulator = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                accumulator += 1 if (((arr[i]*arr[j]) % k) == 0) else 0

        return accumulator
    
    def countPairs(self, nums: List[int], k: int) -> int:
        indices = defaultdict(list)
        pairs_count = 0
        
        for i, num in enumerate(nums):
            indices[num].append(i)
        for key, val in indices.items():
            if len(val) > 1:
                pairs_count += self.check_divisibility(val, k)
            
            
        return pairs_count
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        even = defaultdict(int)
        odd = defaultdict(int)
        size = len(nums)
        for i in range(size):
            if i % 2 == 0: even[nums[i]] += 1
            else: odd[nums[i]] += 1
                
        even = {k: v for k, v in sorted(even.items(), key=lambda item: -item[1])}
        odd = {k: v for k, v in sorted(odd.items(), key=lambda item: -item[1])}
        even = list(even.items())
        odd = list(odd.items())
        print(odd)
        print(even)
        max_even_k, max_even_f = even[0][0], even[0][1]
        max_odd_k, max_odd_f = odd[0][0], odd[0][1]
        
        if len(even) > 1: s_max_e = even[1][1]
        else: s_max_e = 0
        if len(odd) > 1: s_max_o = odd[1][1]
        else: s_max_o = 0
        
        if max_even_k != max_odd_k:
            ans = size - max_even_f - max_odd_f
            
        else:
            
            ans = min(size - max_even_f - s_max_o , size - max_odd_f - s_max_e)
        return ans    
                
        
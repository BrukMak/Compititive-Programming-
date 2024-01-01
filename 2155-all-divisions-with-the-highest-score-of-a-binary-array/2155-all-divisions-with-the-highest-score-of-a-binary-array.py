class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        all_ones = sum(nums)
        seen_ones = [0]
        for i in range(len(nums)):
            num = nums[i]
            if not num:
                seen_ones.append(seen_ones[-1])
            else:
                seen_ones.append(seen_ones[-1]+1)
                
        max_comb = defaultdict(list)
        
        for i in range(len(seen_ones)):
            seen_one = seen_ones[i]
            seen_zero = i - seen_one
            
            ones_in_right = all_ones - seen_one
            max_comb[ones_in_right + seen_zero].append(i)
            
        return max_comb[max(max_comb.keys())]
        
        
        
        
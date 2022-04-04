class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        freq = defaultdict(int)
        for i in nums:
            freq[i] += 1
        
        set_nums = list(freq.keys())
        ans = [0] * len(set_nums)
        
        ans[-1] = set_nums[-1] * freq[set_nums[-1]] 
        for i in range(len(ans)-2, -1, -1):
            if set_nums[i] + 1 < set_nums[i+1]:
                ans[i] = ans[i + 1] + set_nums[i] * freq[set_nums[i]] 
            else:
                if i + 2 < len(ans):
                    temp = ans[i+2] + set_nums[i] * freq[set_nums[i]]
                    ans[i] = max(temp, ans[i+1])
                else:
                    temp = set_nums[i] * freq[set_nums[i]]
                    if i+1 < len(ans):
                        ans[i] = max(temp, ans[i+1])
                    else:
                        ans[i] = temp
           
        return ans[0]
                
            
                
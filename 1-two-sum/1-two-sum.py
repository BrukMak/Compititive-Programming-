class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = defaultdict(list)
        for idx, val in enumerate(nums):
            di[val].append(idx)
        nums.sort()
        
        for idx, val in enumerate(nums):
            l, r = idx+1, len(nums)-1
            while l <= r:
                mid = l + (r-l) // 2
                
                if val + nums[mid] == target:
                    if val == nums[mid]: 
                        return di[val]
                    return [di[val][0], di[nums[mid]][0]]
                    
                elif val + nums[mid] > target:
                    r = mid - 1
                else: l = mid + 1
                
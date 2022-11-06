class Solution:
    def backTrack(self, nums, cur, ans, flag):
        if len(nums) == len(cur):
            ans.append(cur[:])
            return
            
        for i in range(len(nums)):
            check_point = 1 << i
            if not (flag & check_point):
                flag |= check_point
                
                self.backTrack(nums, cur + [nums[i]], ans, flag)
                flag ^= check_point
    def permute(self, nums: List[int]) -> List[List[int]]:
        flag = 0
        ans = []
        self.backTrack(nums, [], ans, flag)
        return ans
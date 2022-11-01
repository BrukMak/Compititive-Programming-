class Solution:
    def backTrack(self, nums, cur, ans,flag):
        if len(nums) == len(cur):
            ans.append(cur[:])
            return
            
        for i in range(len(nums)):
            if not flag[i]:
                flag[i] = True
                self.backTrack(nums, cur + [nums[i]], ans, flag)
                flag[i] = False
            # print(ans)
    def permute(self, nums: List[int]) -> List[List[int]]:
        flag = [False] * len(nums)
        ans = []
        self.backTrack(nums, [], ans, flag)
        return ans
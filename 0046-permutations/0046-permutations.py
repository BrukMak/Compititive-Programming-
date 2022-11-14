class Solution:
    def backTrack(self,index, nums, ans):
        if index == len(nums):
            ans.append(nums[:])
            return
    
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            self.backTrack(index + 1, nums, ans)
            nums[i], nums[index] = nums[index], nums[i] # on back tracking ALWAYS REMEMBER TO RESTORE WHAT You have changed!!!!!!!!!!!!!!!!!!!!!
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backTrack(0, nums, ans)
        return ans
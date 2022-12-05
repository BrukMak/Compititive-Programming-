class Solution:
    def countArrangement(self, n: int) -> int:
        nums = [i for i in range(1, n+1)] # creating the elements
        ans = [0]
        self.countBeautifulArr(0, nums, ans)
        return ans[0]
        
    def countBeautifulArr(self, index, nums, ans):
        if index == len(nums):
            ans[0] += 1
            return 
        
        for i in range(index, len(nums)):
            nums[i], nums[index] = nums[index], nums[i]
            if nums[index] % (index + 1) == 0 or (index + 1) % nums[index] == 0:
                self.countBeautifulArr(index + 1, nums, ans)
            nums[i], nums[index] = nums[index], nums[i]
            
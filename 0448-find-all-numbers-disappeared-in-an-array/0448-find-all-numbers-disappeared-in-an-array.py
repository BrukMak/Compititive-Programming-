class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        # applying quick sort
        
        for i in range(len(nums)):
            
            while i+1 != nums[i]:

                correct = nums[i]-1
                if nums[correct] == nums[i]:
                    break
                nums[i], nums[correct] =  nums[correct] , nums[i]
                
        ans = []                
        for i in range(len(nums)):
            if i + 1 != nums[i]:
                ans.append(i + 1)
        return ans

        
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        # Making the array a linked list. 
        # Marking the seen nodes negative 
        # Collecting when negative is found
        
        res = []
        
        for i, num in enumerate(nums):
            next_num = nums[abs(num)-1]
            if next_num < 0:
                res.append(abs(num))
                continue
            
            nums[abs(num)-1] *= -1
            
        return res
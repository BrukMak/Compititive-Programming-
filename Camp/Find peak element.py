class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums.append(float('-inf'))
        l = 0
        r = len(nums) - 1
        
        while l < r:
            mid = l + (r - l) // 2
            
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1]:
                r = mid - 1
            else:
                l = mid + 1
                
        return l
                

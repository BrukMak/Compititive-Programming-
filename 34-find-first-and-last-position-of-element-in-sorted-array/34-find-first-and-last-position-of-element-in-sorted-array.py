class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = float('inf'), float('inf')
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                cur = mid
                while cur >= 0 and nums[cur] == target:
                    cur -= 1
                start = cur + 1
                while mid < len(nums) and nums[mid] == target:
                    mid += 1
                end = mid - 1
                break
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        if start == float('inf'):
            return [-1, -1]
        else:
            return [start, end]
            
                
            
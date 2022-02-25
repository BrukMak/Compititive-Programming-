class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:        
        ans = []       
        def findPos(bool):
            l = 0
            r = len(nums) - 1
            found = False
            while l <= r:
                mid = l + (r-l)//2

                if target < nums[mid]:
                    r = mid - 1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    if bool:
                        found = True
                        best = mid
                        r = mid - 1
                    else:
                        found = True
                        best = mid
                        l = mid + 1
            if found:
                return best
            else:
                return -1

        ans.append(findPos(True))
        ans.append(findPos(False))
        
        return ans

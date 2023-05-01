class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        def possibleComb(val):
            count = 0
            itera = 0

            while itera < len(nums) - 1:

                if math.fabs(nums[itera] - nums[itera + 1]) <= val:
                    count += 1
                    itera += 2
                else:
                    itera += 1
            if count >= p:
                return True
            return False
    
        def BinarySearch(left , right):
            while left <= right:
                mid = (left + right) // 2
                if possibleComb(mid):
                    right = mid - 1
                    best = mid
                else:
                    left = mid + 1
            return best
        left = 0
        right = (nums[-1] - nums[0])
        best = right
        return BinarySearch(left, right)
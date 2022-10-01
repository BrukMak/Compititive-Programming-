class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        # Finding the number of subarrays that have sum atmost goal
        # 0, 1 ... goal after having that decreament the number of subarrays
        # that have a sum at most goal-1 which gives the number of subarrays
        # with sum equal to goal only
        
        def upToGoal(arr, g):
            if g < 0: return 0
            l, count = 0, 0
            cur = 0
            for r  in range(len(arr)):
                cur += arr[r]
                while cur > g:
                    cur -= arr[l]
                    l += 1
                count += r - l + 1
            return count
        return upToGoal(nums, goal) - upToGoal(nums, goal-1)
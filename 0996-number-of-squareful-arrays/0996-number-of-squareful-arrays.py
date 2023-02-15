class Solution:
    
    def numSquarefulPerms(self, nums: List[int]) -> int:
        res = []

        def findPermutation(nums, current):
            if not nums:
                res.append(current)
                return 

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue

                if current and not self.is_perfect_square(current[-1] + nums[i]):
                    continue

                current.append(nums[i])
                findPermutation(nums[:i] + nums[i + 1:], current)
                current.pop()
        nums.sort()
        findPermutation(nums,[])
        return len(res)

    def is_perfect_square(self,num):
        return pow(int(sqrt(num)),2) == num
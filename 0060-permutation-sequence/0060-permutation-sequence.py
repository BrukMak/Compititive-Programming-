class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Finding all permutation and find the kth => TLE
        
        # The permutation start rom 1 ... n for each has (n! / n) part
        # So find out which part k is
        # do all permutation for (n-1) elements
        # add the group representative to the front on each
        # find the k - (leader - 1)*group_size
        
        nums = [i for i in range(1, n+1)]
        answer = []
        
        self.helper(nums, (k - 1), answer, n) # Since its zero indexed pass (k - 1)
        return "".join(answer)
        
    def helper(self, nums, k, answer, n):
        if len(nums) == 1:
            answer.append(str(nums[0]))
            return answer
        g_size = factorial(n -1)
        target = k // g_size
        answer.append(str(nums[target]))
        nums.remove(nums[target])
        self.helper(nums, k % g_size, answer, n - 1)
        
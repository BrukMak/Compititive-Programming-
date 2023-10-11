class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        mod = 10 ** 9 + 7
        n = len(nums)
        nums.sort()
        ans = 0
        for i in range(n):
            l, r = i, n -1
            val1 = nums[l]
            while r >= l:
                mid = l + (r - l) // 2
                val2 = nums[mid]
                if val1 + val2 <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            # print(r - i)
            if r-i >= 0:
                ans += 2 ** (r - i) % mod
            
        return ans % mod